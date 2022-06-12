#!/bin/sh

FILE="path.py.log"
pip3 --version
echo $(date) >> $FILE
pip3 install --upgrade --target="./local_lib" --log=$FILE git+https://github.com/jaraco/path.git >> $FILE
./my_program.py
