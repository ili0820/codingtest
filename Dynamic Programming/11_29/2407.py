import sys
from math import factorial
input=sys.stdin.readline
n,m=map(int,input().split())
answer=factorial(n)//(factorial(m)*factorial(n-m))
print(answer)
