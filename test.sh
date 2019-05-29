#!/bin/bash

if ! [ "$1" == "" ]; then
	pushd test/ > /dev/null
	python3 $1.py
	pushd > /dev/null
else
	echo "Usage: $0 <test>"
fi