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


n=int(input())
parent=[i for i in range(n+1)]
edges=[]
result=0
temp=[]
for _ in range(n):
    x,y,z=map(int,input().split())
    temp.append((x,y,z,_))

for i in range(3):
    temp=sorted(temp,key=lambda x:x[i])
    for j in range(n):
        c=abs(temp[j-1][i]-temp[j][i])
        edges.append((c, temp[j-1][3],temp[j][3]))


# for i in range(1,n+1):
#     for j in range(i,n+1):
#         c=min(abs(temp[i][0]-temp[j][0]),abs(temp[i][1]-temp[j][1]),abs(temp[i][2]-temp[j][2]))
#         edges.append((c,i,j))

print(edges)
print(len(edges))
edges=sorted(edges)

for edge in edges:
    c,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=c

print(result)
