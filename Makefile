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
	docker exec broker kafka-topics --create --topic audio_subtitles --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
	docker exec broker kafka-topics --create --topic subtitles-audios --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
	docker exec broker kafka-topics --create --topic audio_homero --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1	

build-container:
	sed -i '/^ENVIRONMENT/d' .env
	echo 'ENVIRONMENT=DEPLOYMENT' >> .env
	docker build --no-cache -t reels-automation-prompt-generator .

install-ollama:
	docker exec -it ollama sh -c "ollama pull llama3.2:latest"

python-run:
	sed -i '/^ENVIRONMENT/d' .env
	echo 'ENVIRONMENT=DEVELOPMENT' >> .env
	bash -c 'source env/bin/activate && python main.py'

run-containers:
	sed -i '/^ENVIRONMENT/d' .env
	echo 'ENVIRONMENT=DEPLOYMENT' >> .env
	
	docker run --rm -it \
  --network reels-automation-docker-compose_local-kafka \
  --network reels-automation-docker-compose_ollama-docker \
  reels-automation-prompt-generator

build-run: build-container run-containers

all: install format lint test
