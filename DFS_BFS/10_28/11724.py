# import sys
# from collections import deque
# n,m=map(int,sys.stdin.readline().split())
# graph=[[] for _ in range(n+1)]
# for _ in range(m):
#     x,y=map(int,sys.stdin.readline().split())
#     graph[x].append(y)
#     graph[y].append(x)
#
# visited=[False for _ in range(n+1)]
# def bfs(graph):
#     i=1
#     cnt=0
#     while False in visited:
#         if i>n:
#             break
#         if visited[i]==False:
#             cnt+=1
#             queue=deque([i])
#             visited[i]=True
#             while queue:
#                 v=queue.popleft()
#
#                 for i in graph[v]:
#                     if not visited[i]:
#                         queue.append(i)
#                         visited[i]=True
#         else:
#             i+=1
#     return cnt
# print(bfs(graph))

#BFS
import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited=[False for _ in range(n+1)]

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
cnt=0
for _ in range(1,n+1):
    if not visited[_]:
        bfs(graph,_,visited)
        cnt+=1
print(cnt)

#DFS
import sys
#리미트 안주면 recursion error
sys.setrecursionlimit(10000)
from collections import deque
n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited=[False for _ in range(n+1)]

def dfs(graph,v,visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

cnt=0
for _ in range(1,n+1):
    if not visited[_]:
        dfs(graph,_,visited)
        cnt+=1
print(cnt)