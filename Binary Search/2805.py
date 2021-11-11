import sys
input= sys.stdin.readline
n,m=map(int,input().split())
trees=list(map(int,input().split()))
start,end=0,max(trees)
while start<=end:
    mid=(start+end)//2

    log=0
    log = sum(i - mid  for i in trees if i - mid > 0 )
    if log>=m:
        start=mid+1
    else:
        end=mid-1
print(end)