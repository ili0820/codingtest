import sys
from collections import deque

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[y][x]=True
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<W and 0<=ny<L and graph[ny][nx]==graph[y][x] and not visited[ny][nx]:
                visited[ny][nx]=True
                queue.append((nx,ny))
                
input=sys.stdin.readline
n=int(input())

graph=[]
for _ in range(n):
    graph.append(input().rstrip())

W=len(graph[0])
L=len(graph)

visited=[[False]*W for _ in range(L)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]


cnt1=0
for i in range(W):
    for j in range(L):
        if not visited[j][i]:
            bfs(i,j)
            cnt1+=1

for i in range(L):
    graph[i]=graph[i].replace("G","R")
visited=[[False]*W for _ in range(L)]

cnt2=0
for i in range(W):
    for j in range(L):
        if not visited[j][i]:
            bfs(i,j)
            cnt2+=1



print(cnt1,cnt2)