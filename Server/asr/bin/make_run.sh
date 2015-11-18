#!/bin/bash
cd ../examples/asrdemo
make clean
make

cd ../../bin
rm wav/*.lpcm
rm wav/*.lpcm_done
./asrdemo

