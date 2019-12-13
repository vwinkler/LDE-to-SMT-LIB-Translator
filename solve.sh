#!/bin/bash
python3 translate.py < $1 && echo "" && python3 translate.py < $1 | z3 -in
