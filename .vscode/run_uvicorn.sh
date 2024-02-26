#!/bin/bash

cd $(git rev-parse --show-toplevel)

cd src

pipenv run uvicorn --port 7780  serve_suhweep:app --reload


