setup:
	python3 -m venv venv
	. venv/bin/activate

install:
	pip install -r requirements.txt
	wget https://github.com/hadolint/hadolint/releases/download/v2.12.0/hadolint-Linux-x86_64 -O hadolint && chmod +x hadolint && ./hadolint --version
	curl -s https://api.github.com/repos/anchore/grype/releases/latest | grep \"https.*grype.*linux_amd64.tar.gz\" | cut -d : -f 2,3 | tr -d \\\" | wget -qi - && tar -xvzf grype*.tar.gz grype && rm grype*.tar.gz && ./grype version

lint: 
	python -m pylint app.py
	./hadolint Dockerfile --ignore DL3013 --ignore DL3042

test:
	python -m pytest app.py tests

debug:
	python -m flask run -p 5001 --reload

build:
	docker build -t razorbreak/gotadice-backend:latest .

scan:
	./grype -f critical razorbreak/gotadice-backend:latest

publish:
	docker push razorbreak/gotadice-backend:latest

build-scan-publish: build scan publish

deploy: build
	kubectl apply -f deployment.yml
