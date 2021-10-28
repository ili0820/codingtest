import sys
from collections import deque
r,c=map(int,sys.stdin.readline().split())

visited = [[False] * c for _ in range(r)]
map=[]
for _ in range(r):
    map.append(list(sys.stdin.readline().strip()))
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    global wolves,sheeps
    visited[x][y]=True
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        if map[x][y] == 'v':
            wolves += 1
        if map[x][y] == 'o':
            sheeps += 1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=r or ny >= c or map[nx][ny]=='#':
                continue
            if visited[nx][ny]==False:
                queue.append((nx,ny))
                visited[nx][ny]=True

total_wolves,total_sheeps=0,0

for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            wolves,sheeps=0,0
            bfs(i,j)
            if sheeps>wolves:
                wolves=0
            else:
                sheeps=0
            total_wolves+=wolves
            total_sheeps+=sheeps


print(total_sheeps,total_wolves)