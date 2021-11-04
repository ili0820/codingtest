import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
answer=[0]*10001
#계수 정렬, Count sort
for _ in range(n):
    answer[int(input())]+=1
for _ in range(len(answer)):
    if answer[_]!=0:
        for i in range(answer[_]):
            print(_)