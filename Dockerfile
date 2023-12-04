FROM python:3.11
WORKDIR /api
COPY . . 
RUN pip install -r requirements.txt
RUN pip install gunicorn
CMD ["gunicorn", "--bind=0.0.0.0:5000", "--timeout", "600", "startup:app"]
#ENTRYPOINT [ "/bin/sh" ]
