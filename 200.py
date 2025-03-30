#1 스택

import sys
input = sys.stdin.readline
N = int(input())
stack = []
for i in range(N):
    command = input().split() # command[0] command[1]
    
    if command[0] == "push":