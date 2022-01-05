import sys
input=sys.stdin.readline
n=int(input())
prices=list(map(int,input().split()))
d=[0]*(n+1)
for i in range(1,n+1):
    d[i]=prices[i-1]
for i in range(1,n+1):
    for j in range(1,i+1):
        d[i]=min(d[i-j]+prices[j-1],d[i])

print(d[n])
