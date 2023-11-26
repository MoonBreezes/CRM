# Application entry point
from flask import Flask, render_template, send_from_directory
from flask_marshmallow import Marshmallow
from flask_cors import CORS

from app import models
from app.models.rdb import db
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_restx import Api,Namespace,Resource

ma = Marshmallow()

def create_app(test_config=None) -> Flask:

    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    if( test_config):
        # app.config['TESTING'] = True
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object('config.Config')
    
    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route('/swagger/<path:path>')
    def send_swagger_static(path):
        return send_from_directory('swagger', path)

    db.init_app(app)
    ma.init_app(app)
    
    CORS(app)
    
    with app.app_context():
        db.create_all()  

        from app.routes import nsCliente, nsEnderecoCliente,nsProduto,nsGrupo
      
        api = Api(app, version='1.0', title='Simple CRM', description='API documentation',doc="/swagger")
        api.add_namespace(nsCliente)
        api.add_namespace(nsEnderecoCliente)
        api.add_namespace(nsProduto)
        api.add_namespace(nsGrupo)
        
        return app

app = create_app()