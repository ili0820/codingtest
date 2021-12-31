# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque
# input=sys.stdin.readline
#
#
# def dfs(x, y):
#     if x <= -1 or y <= -1 or x >= n or y >= m:
#         return False
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         dfs(x - 1, y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False
#
# t=int(input())
# for _ in range(t):
#     m,n,k=map(int,input().split())
#
#     graph=[[0 for _ in range(m)] for _ in range(n)]
#
#     for _ in range(k):
#         x,y=map(int,input().split())
#         graph[y][x]=1
#
#     result =0
#     for i in range(n):
#         for j in range(m):
#             if dfs(i,j)==True:
#                 result+=1
#
#     print(result)

import sys
sys.setrecursionlimit(10**6)
from collections import deque
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x, y):
    queue=deque()
    queue.append((x,y))
    while(queue):
        x,y=queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))


t=int(input())
for _ in range(t):
    m,n,k=map(int,input().split())

    graph=[[0]*m for _ in range(n)]

    for _ in range(k):
        x,y=map(int,input().split())
        graph[y][x]=1

    result =0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                bfs(i,j)
                graph[i][j]=0
                result+=1

    print(result)