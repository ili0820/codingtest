import sys
input=sys.stdin.readline
n=int(input())
As=list(map(int,input().split()))

d=[n+1]*n
d[0]=0

for i in range(n):
    for j in range(1,As[i]+1):
        if i+j>=n:
            break
        d[i+j]=min(d[i+j],d[i]+1)
print(d[n-1] if d[n-1]!=n+1 else -1)