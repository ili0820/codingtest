# import sys
# input=sys.stdin.readline
#
# n=int(input())
# numbs=sorted(list(map(int,input().split())))
# m=int(input())
# tests=list(map(int,input().split()))
#
# def left_binary(s,e,t,a):
#     while(s<e):
#         m = (s + e) // 2
#         if a[m] >= t:
#             e=m
#         else:
#             s=m+1
#     return s
#
# def right_binary(s,e,t,a):
#     while(s<e):
#         m = (s + e) // 2
#         if a[m] > t:
#             e=m
#         else:
#             s=m+1
#     return s
#
# for t in tests:
#     print(right_binary(0,n,t,numbs)-left_binary(0,n,t,numbs),end=" ")
from collections import Counter
import sys
input=sys.stdin.readline

n=int(input())
numbs=list(map(int,input().split()))
m=int(input())
tests=list(map(int,input().split()))

counts=Counter(numbs)
for t in tests:
    print(counts[t],end=' ')

#COUNTER 가 1020ms 으로 약 4배 더 빨랐다.