#!/usr/bin/python
# -*- coding: utf-8 -*-
from solver import solve
from os import listdir
import json
if __name__ == '__main__':
    solution = []
    for i in listdir('data'):
        solution.append({'file':i,'solution':solve(f'data/{i}')})
    print(json.dumps(solution))