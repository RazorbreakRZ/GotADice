[![Docker](https://dl.circleci.com/status-badge/img/gh/RazorbreakRZ/GotADice/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/RazorbreakRZ/GotADice/tree/main)

# GotADice
A simple project that test a full CI/CD pipeline. The steps made in behind fulfill most common task:
- Local environment setup
- Code build, testing & linting (using pytest and pylint)
- Docker build, vulnerability scan & push to registry
- Continuous delivery to runtime environment (rolling update)
- Smoke testing
- Rollback management

## Development environment setup
Ensure that `Python 3.10+` is installed in your computer.
```bash
python3 -m venv venv
source venv/bin/activate
```

## Run python app
```bash
flask run --reload
```

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

Then deploy and configure at least a cluster (or use an existing one):
```bash

```