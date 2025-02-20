#!/usr/bin/env bash

echo "Updating repository."
git pull origin master

echo "Installing dependencies."
source ./bin/install.sh

echo "Running Mongo database."
./.database/bin/mongod --dbpath ./.database/db

echo "Running main script."
./.venv/bin/python ./main.py

