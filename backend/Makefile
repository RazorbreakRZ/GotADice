setup:
	python3 -m venv ~/.gotadice
	# source ~/.gotadice/bin/activate

install:
	pip install -r requirements.txt
	wget https://github.com/hadolint/hadolint/releases/download/v2.12.0/hadolint-Linux-x86_64 -O hadolint && chmod +x hadolint

lint: 
	python -m pylint app.py
	./hadolint Dockerfile

test:
	python -m pytest app.py tests

debug:
	python -m flask run --reload

build:
	docker build -t razorbreak/gotadice:latest .

publish:
	docker push razorbreak/gotadice:latest

build-and-publish: build publish