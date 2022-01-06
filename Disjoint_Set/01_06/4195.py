import sys
input=sys.stdin.readline

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b,cnt):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a!=b:
        parent[b]=a
        cnt[a]+=cnt[b]

n=int(input())

for _ in range(n):
    f=int(input())
    parent={}
    cnt={}
    for __ in range(f):
        f1,f2=input().split()

        if f1 not in parent:
            parent[f1]=f1
            cnt[f1]=1
        if f2 not in parent:
            parent[f2]=f2
            cnt[f2]=1

        union_parent(parent,f1,f2,cnt)
        print(cnt[find_parent(parent,f1)])