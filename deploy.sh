#!/bin/bash

PORT=/dev/ttyACM0
DIR=/home/adrian/Dev/adistools-rei

ampy --port $PORT rm /flash/main.py
ampy --port $PORT rm /flash/boot.py
ampy --port $PORT rm /flash/map.py
ampy --port $PORT rm /flash/payload.json


ampy --port $PORT put $DIR/main.py 
ampy --port $PORT put $DIR/boot.py 
ampy --port $PORT put $DIR/map.py
ampy --port $PORT put $DIR/payload.json