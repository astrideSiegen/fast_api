#!/bin/bash

# Build and run tests
docker-compose down
docker-compose build
docker-compose up