#!/usr/bin/python
# -*- coding: utf-8 -*-
from solver import solve
def check():
    dic = { 
        'data/ks_30_0'     : 'best-result/problem1-10pt.txt',
        'data/ks_50_0'     : 'best-result/problem2-10pt.txt',
        'data/ks_200_0'    : 'best-result/problem3-10pt.txt',
        'data/ks_400_0'   : 'best-result/problem4-10pt.txt',
        'data/ks_1000_0'   : 'best-result/problem5-10pt.txt',
        'data/ks_10000_0' : 'best-result/problem6-10pt.txt'
    }
    for i,j in dic.items():
        answer = solve(i)
        print(f'{i}:',end=' ')
        with open(j,'r') as f:
            best_solution = int(f.readline().split(' ')[0])
            print(f'ortools solution: {answer["objective"]}, best solution: {best_solution}',end='')
        print()
if __name__ == '__main__':
    check()
