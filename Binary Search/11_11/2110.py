import sys
input=sys.stdin.readline
n,c= map(int,input().split())
pos=[]
for _ in range(n):
    pos.append(int(input()))
pos=sorted(pos)
start,end=0,pos[-1]-pos[0]

result=0
while(start<=end):
    mid=(start+end)//2
    old=pos[0]
    cnt=1

    for i in range(1,n):
        if pos[i]>=old+mid:
            cnt+=1
            old=pos[i]
    if cnt>=c:
        start=mid+1
        result=mid
    else:
        end=mid-1
print(result)