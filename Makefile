install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py tema/*.py
lint:
	pylint --disable=R,C *.py tema/*.py
test:
	# python -m pytest -vv --cov=logic
build:
	# build docker
run:
	#run docker
deploy:
	#deploy
all: install format lint test build deploy
