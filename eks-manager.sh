#!/bin/bash

REGION=us-west-2
CLUSTER_NAME=udacity
PROJECT_NAME=gotadice

case $1 in
    create)
        eksctl create cluster -n udacity --tags project=$PROJECT_NAME --region $REGION --nodes 2 --node-type t3a.small
    ;;
    delete)
        eksctl delete cluster -n udacity --region $REGION
    ;;
    *)
        echo "Invalid option \"$1\". Valid ones are: create | delete"
    ;;
esac
