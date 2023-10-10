setup:
	python3 -m venv venv
	. venv/bin/activate

install:
	pip install -r requirements.txt
	wget https://github.com/hadolint/hadolint/releases/download/v2.12.0/hadolint-Linux-x86_64 -O hadolint && chmod +x hadolint && ./hadolint --version
	curl -s https://api.github.com/repos/anchore/grype/releases/latest | grep \"https.*grype.*linux_amd64.tar.gz\" | cut -d : -f 2,3 | tr -d \\\" | wget -qi - && tar -xvzf grype*.tar.gz grype && rm grype*.tar.gz && ./grype version
	curl -LO https://dl.k8s.io/release/v1.27.2/bin/linux/amd64/kubectl && chmod +x kubectl && ./kubectl version --client
	
lint: 
	python -m pylint app.py
	./hadolint Dockerfile --ignore DL3013 --ignore DL3042

test:
	python -m pytest app.py tests

debug:
	python -m flask run -p 5000 --reload

build:
	docker build -t razorbreak/gotadice:latest .

scan:
	./grype -f critical razorbreak/gotadice:latest

publish:
	docker push razorbreak/gotadice:latest

build-scan-publish: build scan publish

validate-service: build
	docker run --name gotadice -d -p 5000:5000 razorbreak/gotadice:latest
	@sleep 10
	chmod +x validate-service.sh && ./validate-service.sh localhost:5000
	docker rm -f gotadice

deploy: build
	kubectl apply -f deployment.yml
