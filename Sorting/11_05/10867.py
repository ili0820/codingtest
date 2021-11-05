import sys

input=sys.stdin.readline
n=int(input())
numbers=sorted(list(set(map(int,input().split()))))

for _ in numbers:
    print(_,end=" ")