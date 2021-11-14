import sys
input=sys.stdin.readline
x,y=map(int,input().split())
z=y*100//x

s=1
e= 1000000000
ans=e
if z>=99:
    print(-1)
else:
    while(s<=e):
        m=(s+e)//2

        if  (y+m)*100//(x+m)>z:
            ans=min(ans,m)
            e=m-1
        else:
            s=m+1
    print(ans)

