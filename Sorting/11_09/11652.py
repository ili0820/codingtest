import sys
from collections import Counter
input=sys.stdin.readline
n=int(input())
numbs=[int(input()) for _ in range(n)]
numbs=Counter(numbs).most_common()
numbs=sorted(numbs,key=lambda x : (-x[1],x[0]))

print(numbs[0][0])