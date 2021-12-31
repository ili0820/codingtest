import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
t=int(input())



def dfs(x,y):
    if 0 <= x < h and 0 <= y < w and visited[x][y] == False and graph[x][y] == "#":
        visited[x][y] = True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(nx,ny)


dx=[-1,1,0,0]
dy=[0,0,-1,1]
for _ in range(t):
    h,w=map(int,input().split())
    graph=[]
    cnt=0
    visited = [[False] * w for _ in range(h)]
    for _ in range(h):
        graph.append(list(input().strip()))
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j]=='#':
                dfs(i,j)
                cnt+=1
    print(cnt)


import sys
from collections import deque
input=sys.stdin.readline
t=int(input())



def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w and visited[nx][ny]==False and graph[nx][ny]=="#":
                queue.append((nx,ny))
                visited[nx][ny]=True


dx=[-1,1,0,0]
dy=[0,0,-1,1]
for _ in range(t):
    h,w=map(int,input().split())
    graph=[]
    cnt=0
    visited = [[False] * w for _ in range(h)]
    for _ in range(h):
        graph.append(list(input().strip()))
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j]=='#':
                bfs(i,j)
                cnt+=1
    print(cnt)
