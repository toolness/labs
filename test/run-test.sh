#! /bin/bash

docker-compose stop && docker-compose rm -f && \
  docker-compose run home python test_util.py
