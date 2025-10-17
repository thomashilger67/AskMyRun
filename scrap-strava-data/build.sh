#!/bin/bash

docker build -t scrap-askmyrun --build-arg STRAVA_ACCESS_TOKEN --build-arg DATE .
docker tag scrap-askmyrun:latest europe-west9-docker.pkg.dev/strava-llm/my-registry/scrap-askmyrun:latest
docker push europe-west9-docker.pkg.dev/strava-llm/my-registry/scrap-askmyrun:latest