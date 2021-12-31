from collections import deque
import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for _ in range(n+1):
    graph[_]=sorted(graph[_])

def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,v,visited):
    queue=deque([v])
    visited[v]=True
    while queue:
        v=queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

dfs(graph,v,visited)
visited=[False]*(n+1)
print()
bfs(graph,v,visited)