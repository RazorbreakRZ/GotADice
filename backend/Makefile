setup:
	python3 -m venv ~/.gotadice
	source ~/.gotadice/bin/activate

install:
	wget https://github.com/hadolint/hadolint/releases/download/v2.12.0/hadolint-Linux-x86_64 -O /bin/hadolint && chmod +x /bin/hadolint
	pip install -r requirements.txt

lint: 
	hadolint Dockerfile
	pylint --disable=R,C,W1203,W1202,W1508,W1309 app.py

debug:
	flask run --reload

build:
	docker build -t razorbreak/gotadice:latest .

publish:
	docker push razorbreak/gotadice:latest

build-and-publish: build publish