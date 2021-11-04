import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
answer=[]
for _ in range(n):
    answer.append(int(input()))
for _ in sorted(answer):
    print(_)