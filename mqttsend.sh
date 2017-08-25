#!/bin/bash
ownPath="$(readlink -f "$0")"
ownFolder="$(dirname "$ownPath")"
cd $ownFolder

source bin/activate

bin/python3.6 mqttsend.py