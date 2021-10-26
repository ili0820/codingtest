import sys
from collections import deque
n=int(input())
a,b=map(int,sys.stdin.readline().split())
m=int(input())
relations=[]
for _ in range(m):
    relations.append(list(map(int,sys.stdin.readline().split())))
visited=[False for _ in range(n+1)]
graph=[[] for _ in range(n+1)]
dist=[0 for _ in range(n+1)]

for x,y in relations:
    graph[x].append(y)
    graph[y].append(x)

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                #책의 코드와 이 부분 빼고 동일.
                dist[i]=dist[v]+1
                visited[i]=True

bfs(graph,a,visited)
print(dist)
print(dist[b] if not dist[b]==0 else -1)


