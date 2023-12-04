main: help

run:
	./run.sh

lizard:
	lizard app -o quality.html

test: FORCE
	python -m unittest discover -s test/unit -p '*_test.py'

FORCE:


tag=engsoft:latest

dedit:
	nano Dockerfile

dbuild:
	docker build . --tag $(tag)

drun:
	docker run -p 5000:5000 -it $(tag)

help:
	cat Makefile
