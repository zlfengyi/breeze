#!/usr/bin/bash

cd ../examples/ttsdemo
make clean
make
cd ~/breeze/tts/bin
./ttsdemo
