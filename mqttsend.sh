#!/bin/bash
cd $(dirname "${BASH_SOURCE[0]}")

if [ -f "bin/activate" ]; then
    source bin/activate
    if [ ! -f "bin/python3" ]; then
        echo "No python3 binary found." >&2
        exit 1
    fi
    python_exec="bin/python3"
elif [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
    if [ ! -f "venv/bin/python3" ]; then
        echo "No python3 binary found." >&2
        exit 1
    fi
    python_exec="venv/bin/python3"
else
	echo "No venv found. Please make one!" >&2
	exit 1
fi

$python_exec mqttsend.py >> mqttsend.log  2>&1
