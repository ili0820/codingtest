import sys

input=sys.stdin.readline

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a > b:
        parent[a]=b
    else:
        parent[b]=a

n=int(input())
m=int(input())
parent=[i for i in range(n+1)]
edges=[]
result=0
for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))

edges=sorted(edges)

for edge in edges:
    c,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=c
print(result)