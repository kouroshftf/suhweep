#!/bin/bash

cd $(git rev-parse --show-toplevel)

cd src

uvicorn --port 7780  serve_suhweep:app --reload


