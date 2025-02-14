#!/usr/bin/env bash

echo "Updating repository."
git pull origin master

echo "Installing dependencies."
source ./bin/install.sh

echo "Running main script."
./.venv/bin/python ./main.py
