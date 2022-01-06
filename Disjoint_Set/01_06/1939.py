#Kruskal's algorithm
import sys
input=sys.stdin.readline

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m=map(int,input().split())

parent=[i for i in range(n+1)]
edges=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))

edges=sorted(edges,reverse=True)

start,end=map(int,input().split())
for edge in edges:
    c,a,b=edge
    union_parent(parent,a,b)
    if find_parent(parent,start)==find_parent(parent,end):
        print(c)
        break



