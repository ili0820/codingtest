import sys
input=sys.stdin.readline
t=int(input())
def bin(s,e,t,Bs):
    idx=-1
    while(s<=e):
        mid=(s+e)//2
        if Bs[mid] <t:
            idx=mid
            s=mid+1
        else:
            e=mid-1
    return idx

for _ in range(t):
    n,m=map(int,input().split())
    As=sorted(list(map(int,input().split())))
    Bs=sorted(list(map(int,input().split())))
    s = 0
    e = m - 1
    cnt=0
    for a in As:
        cnt+=bin(s, e, a,Bs) +1
    print(cnt)


# 1 1 3 7 8
# 1 3 6





# 2 7 13
