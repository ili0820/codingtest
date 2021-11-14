import sys
input=sys.stdin.readline
n,m=map(int,input().split())

time=sorted([int(input()) for _ in range(n)])

s=min(time)
e=max(time)*m
ans=e
while(s<=e):
    total=0
    mid=(s+e)//2

    for t in time:
        total+=mid//t
    if total >=m:
        e=mid-1
        ans=min(ans,mid)
    else:
        s=mid+1
print(ans)