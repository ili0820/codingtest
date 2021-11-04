import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
answer=[]
for _ in range(n):
    answer.append(int(input()))
answer.sort()
for _ in answer:
    print(_)