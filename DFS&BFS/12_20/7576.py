from collections import deque
import sys
input=sys.stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0]
m,n=map(int,input().split())
array=[ list(map(int,input().split())) for x in range(n)]
queue = deque()
for i in range(n):
    for j in range(m):
        if array[i][j]==1:
            queue.append([i, j])

cnt=0
def bfs(array):

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and array[nx][ny]==0:
                array[nx][ny]=array[x][y]+1
                queue.append((nx,ny))





bfs(array)
ans=0
for i in array:
    for j in i:
        if j==0:

            ans=int(1e9)
            break
    ans=max(ans,max(i))
print(ans-1 if ans!=int(1e9) else -1)