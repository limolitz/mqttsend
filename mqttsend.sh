#!/bin/bash
cd $(dirname "${BASH_SOURCE[0]}")

if [ ! -f "bin/activate" ]; then
	echo "No venv found. Please make one!" >&2
	exit 1
fi

source bin/activate


if [ -f "bin/python3.6" ]; then
	bin/python3.6 mqttsend.py >> mqttsend.log 2>&1
elif [ -f "bin/python3.5" ]; then
	bin/python3.5 mqttsend.py >> mqttsend.log 2>&1
elif [ -f "bin/python3" ]; then
	bin/python3 mqttsend.py >> mqttsend.log  2>&1
else
	echo "No python3 binary found."
fi
