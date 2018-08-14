#!/bin/bash
Tag=$1
if [ "$Tag" == "" ] ; then
    echo "Tag value cannot be empty"
    exit 1
fi
export imageTag=$Tag

echo "Stopping service container"
docker-compose -f docker-compose-run.yml stop

echo "Starting service container"
docker-compose -f docker-compose-run.yml up -d