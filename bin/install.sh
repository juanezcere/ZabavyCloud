#!/usr/bin/env bash

# Install git
# Install Python3
# Install NodeJS

echo "Creating environment."
python3 -m venv ./.venv

echo "Installing Python dependencies."
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/pip install -r requirements.txt

echo "Installing NodeJS dependencies."
npm install

echo "Building the project."
source ./bin/build.sh
