install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py tema/*.py
lint:
	pylint --disable=R,C *.py tema/*.py
test:
	python -m pytest -vv --cov=tema

create-topics:
	
# Este primer kafka quizas esté demas crearlo acá 

	docker exec broker kafka-topics --create --topic temas --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 
	docker exec broker kafka-topics --create --topic scripts_video --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

run-containers:
# docker-compose -f docker-compose-ollama-gpu.yaml up -d
# docker compose up -d

all: install format lint test

# kafka-topics.bat --create --bootstrap-server localhost:9092 --topic scripts_video
