#!/bin/bash
Tag=$1
if [ "$Tag" == "" ] ; then
    echo "Tag value cannot be empty"
    exit 1
fi

echo "Building image"
docker-compose -f docker-compose.yml build

echo "Tagging image with tag: $Tag"
docker tag rahullodha85/python-practice_web:latest rahullodha85/python-practice_web:$Tag

echo "Pushing image rahullodha85/python-practice_web:$Tag"
docker push rahullodha85/python-practice_web:$Tag