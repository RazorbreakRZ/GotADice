[![Docker](https://dl.circleci.com/status-badge/img/gh/RazorbreakRZ/GotADice/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/RazorbreakRZ/GotADice/tree/main)

# GotADice
A simple project that test a full CI/CD pipeline. The steps made in behind fulfill most common task:
- Local environment setup (with Makefile)
- Code build, testing & linting (using PyTest and PyLint)
- Docker build (CircleCI), vulnerability scan (with Anchore Grype) & push to registry (DockerHub)
- Continuous delivery to runtime environment (rolling update with replicasets) into sandbox EKS cluster (pre-deployed with eksctl)
- Smoke testing against service (validate-service.sh)
- Rollback management (if smoke testing fails)

## Development environment setup
Ensure that `Python 3.10+` is installed in your computer.
```bash
python3 -m venv venv
source venv/bin/activate
```

## Run python app locally
```bash
cd service
make debug
```
And access `http://localhost:5000`

A web page showing a Dice should appear with the release version at the top left corner and a button at the bottom. Every time the button is pressed, the dice is rolled and the result is generated randomly by the `/roll` endpoint.

The linting process of the application and its related Dockerfile are made by PyLint and Hadolint. This step can be done locally using the `make lint` at the same folder level.

And for unit testing, don't forget to try `make test` to run the unit tests located in `service/tests` folder.

## Runtime environment setup
As a runtime to deploy the application, I used AWS EKS to deploy a managed k8s cluster with eksctl (easiest method). To install the eksctl tool, you can follow the following steps (**only for Unix systems!**):
```bash
# for ARM systems, set ARCH to: `arm64`, `armv6` or `armv7`
ARCH=amd64
PLATFORM=$(uname -s)_$ARCH

curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz"

# (Optional) Verify checksum
curl -sL "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_checksums.txt" | grep $PLATFORM | sha256sum --check

tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz

sudo mv /tmp/eksctl /usr/local/bin

eksctl version
```
For other OS, please refer to official documentation at https://eksctl.io/introduction/#installation

Then deploy and auto-configure a small sandbox cluster you can run the provided script. Edit the `eks-manager.sh` script to meet any additional requirements:
```bash
# To create a new cluster named 'udacity' with 2 nodes in 'eu-west-1' region and version '1.27':
./eks-manager.sh create
# To cleanup resources:
./eks-manager.sh cleanup
# And to delete it:
./eks-manager.sh delete
```
To prevent any kind of stucked resource, remember to cleanup the cluster resources (like LoadBalancers) prior to removing the AWS ones!

The `make install` will also download the kubectl application locally to the project folder. This way the version will match the ControlPlane one of K8s.

## Useful links
- DockerHub image location: https://hub.docker.com/r/razorbreak/gotadice/tags
- CircleCI pipeline: https://app.circleci.com/pipelines/github/RazorbreakRZ/GotADice
