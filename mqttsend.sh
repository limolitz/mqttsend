#!/bin/bash
cd $(dirname "${BASH_SOURCE[0]}")

if [ ! -f "bin/activate" ]; then
	echo "No venv found. Please make one!"
	exit
fi

source bin/activate


if [ -f "bin/python3.6" ]; then
	bin/python3.6 mqttsend.py
elif [ -f "bin/python3.5" ]; then
	bin/python3.5 mqttsend.py
elif [ -f "bin/python3" ]; then
	bin/python3 mqttsend.py
else
	echo "No python3 binary found."
fi
