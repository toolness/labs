#! /bin/bash

python convert_to_pydoctest.py &&
  docker-compose stop && docker-compose rm -f && \
  docker-compose run home python test_util.py
