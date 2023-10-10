#!/bin/bash

REGION="eu-west-1"
CLUSTER_VERSION="1.27"
CLUSTER_NAME="udacity"
CLUSTER_SIZE=2
CLUSTER_INSTANCE_TYPE="t3a.small"
PROJECT_NAME="gotadice"

case $1 in
    create)
        eksctl create cluster -n $CLUSTER_NAME --tags project=$PROJECT_NAME --region $REGION --nodes $CLUSTER_SIZE --node-type $CLUSTER_INSTANCE_TYPE --version=$CLUSTER_VERSION
    ;;
    delete)
        eksctl delete cluster -n $CLUSTER_NAME --region $REGION
    ;;
    *)
        echo "Invalid option \"$1\". Valid ones are: create | delete"
    ;;
esac
