#!/usr/bin/env bash

# Change to script directory
cd "`dirname "$0"`"

python3 -m venv venv

./venv/bin/pip3 install -r requirements.txt
