import sys
from collections import deque
input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().strip())))

def bfs(x,y):
    cnt=1
    queue=deque()
    queue.append((x,y))
    while(queue):
        x,y=queue.popleft()
        graph[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny] = 0
                cnt+=1
    return cnt

answer=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            answer.append(bfs(i,j))
print(len(answer))
for _ in sorted(answer):
    print(_)