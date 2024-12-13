init:
	@echo "initialization...";
	@echo "Creation d'un environnement virtuel"; \
	python3 -m venv .venv; \
	. .venv/bin/activate && \
	echo "Installer les librairies" && \
	pip install -r requirements.txt

run:
	. .venv/bin/activate && \
	python3 app.py

build:
	docker build -t monimage .

test:
	. .venv/bin/activate && \
	python3 test_health_utils.py

test-api:
	curl -X POST -H "Content-Type: application/json" -d '{"weight": 70, "height": 1.75}' http://localhost:5000/bmi
	curl -X POST -H "Content-Type: application/json" -d '{"weight": 70, "height": 175, "age": 30, "gender": "male"}' http://localhost:5000/bmr

stop-app:
	. .venv/bin/activate && \
	pkill -f app.py

run-container:
	docker run -p 5001:5000 monimage