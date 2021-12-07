import sys
input=sys.stdin.readline
INF=int(1e9)

n,d=map(int,input().split())
graph=dict()
temp=[]



for _ in range(n):
    x,y,z=map(int,input().split())
    temp.append((x,y,z))
    graph[x]=[]

for _ in temp:
    graph[_[0]].append((_[1],_[2]))
print(graph)

distance=[i for i in range(d+1)]

for i in range(d+1):
    distance[i]=min(distance[i],distance[i-1]+1)
    if i in graph:
        for y,z in graph[i]:
            if y<=d and distance[y]>distance[i]+z:
                distance[y]=distance[i]+z

print(distance[d])


