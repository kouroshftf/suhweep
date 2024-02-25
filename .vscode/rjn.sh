#!/bin/bash

# may need these first:
# pipenv install --dev

# to drop venv and create new one:
# pipenv --rm
# pipenv shell


# -----------------------------------------

export HISTFILE='/dev/null'
export HISTSIZE=20
# unset HISTFILE

export PYSPARK_PYTHON="python3"
export SPARK_LOCAL_IP="127.0.0.1"

export CURR_REPO_ROOT="$(git rev-parse --show-toplevel)"
# echo $CURR_REPO_ROOT

pipenv run jupyter lab "$CURR_REPO_ROOT" --no-browser --ip 127.0.0.1 --port 7632