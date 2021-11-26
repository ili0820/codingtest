import sys
from collections import deque
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

dx=[-1,1,0,0,-1,1,-1,1]
dy=[0,0,-1,1,-1,1,1,-1]

def dfs(y,x):
    if x<0 or x>=w or y<0 or y>=h:
        return False
    if array[y][x]==1:
        array[y][x]=0
        dfs(y - 1, x - 1)
        dfs(y - 1, x)
        dfs(y - 1, x + 1)
        dfs(y, x - 1)
        dfs(y, x + 1)
        dfs(y + 1, x - 1)
        dfs(y + 1, x)
        dfs(y + 1, x + 1)
        return True
    return False

def bfs(y,x):
    queue=deque()
    queue.append((y,x))
    while queue:
        y,x=queue.popleft()
        visited[y][x]=True
        for i in range(8):
            nx= x + dx[i]
            ny= y + dy[i]
            if nx<0 or ny<0 or ny>=h or nx>=w:
                continue
            if not visited[ny][nx]:
                visited[ny][nx]=True
                if array[ny][nx]==1:
                    queue.append((ny,nx))


while(1):
    w,h=map(int,input().split())
    if w==h==0:
        break
    array=[list(map(int,input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]


    # result=0
    # for i in range(h):
    #     for j in range(w):
    #         if not visited[i][j] and array[i][j]==1:
    #             bfs(i,j)
    #             result+=1
    # print(result)

    result=0
    for i in range(h):
        for j in range(w):
            if dfs(i,j):
                result+=1
    print(result)




