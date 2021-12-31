import sys
from collections import deque
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(input().strip()))
visited=[[False]*m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0
def dfs(x,y):
    global cnt
    if 0 <= x < n and 0 <= y < m and visited[x][y] == False and graph[x][y] != 'X':
        visited[x][y]=True
        if graph[x][y]=='P':
            cnt+=1

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(nx,ny)

index=[(i,j) for i in range(n) for j in range(m) if graph[i][j]=='I']
dfs(index[0][0],index[0][1])
print("TT" if cnt==0 else cnt)



import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(input().strip()))
visited=[[False]*m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0
def bfs(index):
    x,y=index[0][0],index[0][1]
    global cnt
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False and graph[nx][ny]!='X':
                visited[nx][ny]=True
                if graph[nx][ny]=='P':
                    cnt+=1
                queue.append((nx,ny))


index=[(i,j) for i in range(n) for j in range(m) if graph[i][j]=='I']
bfs(index)
print("TT" if cnt==0 else cnt)


