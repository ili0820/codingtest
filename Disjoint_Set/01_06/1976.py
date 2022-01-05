import sys
from collections import Counter
input=sys.stdin.readline
n=int(input())
m=int(input())
parent=[i for i in range(n+1)]

def ver(temp):
    for i in range(m - 1):
        if parent[temp[i]] != parent[temp[i + 1]]:
            return "NO"
    return "YES"

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
for i in range(n):
    temp=list(map(int,input().split()))
    for j in range(n):
        if temp[j]==1:
            union_parent(parent,i+1,j+1)

temp=list(map(int,input().split()))
print(len(temp) - 1)
print(parent)
print(temp)
print(ver(temp))