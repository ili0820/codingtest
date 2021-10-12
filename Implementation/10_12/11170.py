# import sys
# t=int(input())
# for _ in range(t):
#     n,m=map(int,sys.stdin.readline().split())
#     numbers=list(range(n,m+1))
#     cnt=0
#     for numb in numbers:
#         for _ in str(numb):
#             if _ =="0":
#                 cnt+=1
#     print(cnt)

from collections import Counter
import sys

t=int(input())
for _ in range(t):
    n,m=map(int,sys.stdin.readline().split())
    numbers="".join([str(x) for x in range(n,m+1)])
    print(Counter(numbers)["0"])