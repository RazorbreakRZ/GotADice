#!/bin/bash

URL=$1
ERRORS=0

if [ -z "${URL}" ];then
    echo "Invalid or missing URL to test!"
    exit 255
fi

echo "Validating service at [${URL}]:"

echo -n "Testing HTML is returned........"
curl -s -f -o /dev/null "${URL}"
if [[ $? > 0 ]];then
    ERRORS=$(expr $ERRORS + 1)
    echo "ERROR"
else
    echo "OK"
fi

echo -n "Testing healthcheck endpoint...."
curl -s -f -o /dev/null "${URL}/info"
if [[ $? > 0 ]];then
    ERRORS=$(expr $ERRORS + 1)
    echo "ERROR"
else
    echo "OK"
fi

echo -n "Testing other endpoints........."
curl -s -f -o /dev/null "${URL}/roll"
if [[ $? > 0 ]];then
    ERRORS=$(expr $ERRORS + 1)
    echo "ERROR"
else
    echo "OK"
fi

echo "Final results: [$ERRORS] errors detected"
if [[ $ERRORS > 0 ]];then
    exit 1
fi
