#!/bin/bash

mkdir characters
python3 -m venv character-venv
source character-venv/bin/activate
pip3 install -r requirements.txt
clear
pytest test.py