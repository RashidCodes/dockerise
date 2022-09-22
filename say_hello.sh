#!/bin/bash

image_name="test"
docker rm -f ${image_name} > /dev/null
docker run -e NAME="rashid" -e API_KEY=${API_KEY} -e CITY="canberra" --name ${image_name} my_hello_world
