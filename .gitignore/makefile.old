ports = 5000;
init :
	python3 -m venv .venv;
	. .venv/bin/activate && \
 	pip install -r requirements.txt

run :
	. .venv/bin/activate && \
	python3 app.py

build : 
	docker build -t papp . 

test :
	. .venv/bin/activate && \	
	python3 test.py
test-api: 
	curl http://
build-image:
	docker run -d -p 5000:5000 papp
