import sys
from collections import deque
input=sys.stdin.readline
m,n=map(int,input().split())
graph=[]
for _ in range(m):
    graph.append(list(map(int,input().strip().split())))
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]

visited=[[False]*n for _ in range(m)]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and visited[nx][ny]==False and graph[nx][ny]==1:
                queue.append((nx,ny))
                visited[nx][ny] = True
cnt=0
for i in range(m):
    for j in range(n):
        if graph[i][j]==1 and not visited[i][j]:
            bfs(i,j)
            cnt+=1
print(cnt)
