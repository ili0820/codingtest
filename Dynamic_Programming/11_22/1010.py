import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    ans=1
    k=n-m
    while(n>k):
        ans*=n
        n-=1
    while(m>1):
        ans//=m
        m-=1
    print(ans)
#
# import math
#
# T = int(input())
#
# for _ in range(T):
#     n, m = map(int, input().split())
#     bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
#     print(bridge)