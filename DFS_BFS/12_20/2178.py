from collections import deque
import sys

n,m=map(int,input().split())
graph=[]
for _ in range(n):
  graph.append(list(map(int, input())))

dx=[0,0,1,-1]
dy=[-1,1,0,0]
def bfs():
    queue=deque()
    queue.append((0,0))
    while(queue):
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))




bfs()
print(graph[n-1][m-1])

