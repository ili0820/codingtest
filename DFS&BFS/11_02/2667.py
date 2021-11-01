import sys
sys.setrecursionlimit(10**6)
from collections import deque
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x, y,t):
    global cnt
    if 0<=x<t and 0<=y<t and graph[x][y]==1:
        cnt+=1
        graph[x][y]=0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny,t)
        return True
    return False

t=int(input())
graph=[]
answer=[]
cnt=0
for _ in range(t):
    graph.append(list(map(int,input().strip())))
for i in range(t):
    for j in range(t):
        if dfs(i,j,t):
            answer.append(cnt)
            cnt=0

print(len(answer))
answer.sort()
for _ in answer:
    print(_)
#
# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque
# input=sys.stdin.readline
#
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
#
# def bfs(x, y,t):
#     numbers=1
#     queue=deque()
#     queue.append((x,y))
#     graph[x][y] = 0
#     while(queue):
#         x,y=queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<t and 0<=ny<t and graph[nx][ny]==1:
#                 numbers += 1
#                 graph[nx][ny]=0
#                 queue.append((nx,ny))
#     return numbers
#
# t=int(input())
# graph=[]
# answer=[]
# for _ in range(t):
#     graph.append(list(map(int,input().strip())))
# for i in range(t):
#     for j in range(t):
#         if graph[i][j] ==1:
#             answer.append(bfs(i,j,t))
#
# print(len(answer))
# answer.sort()
# for _ in answer:
#     print(_)