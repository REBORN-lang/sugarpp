#!/usr/bin/env bash

g++ -std=c++23 ./examples/transpiled/calculator.cpp -o ./test
gcc -std=c23 ./examples/transpiled/calculator.c -o ./testc -lm
