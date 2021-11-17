import sys
input=sys.stdin.readline
M,n=map(int,input().split())
cookies=list(map(int,input().split()))

s=0
e=max(cookies)

answer=0
while(s<=e):
    cnt = 0
    m=(s+e)//2
    if m ==0:
        cnt=0
        break
    for x in cookies:
        if x>=m:
            cnt+=(x//m)
    if cnt>=M:
        s=m+1
        answer=m
    else:
        e=m-1
print(answer)