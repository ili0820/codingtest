from collections import deque
import sys
n=int(input())
board = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
#Shallow copy로 오류를 범하지말자.
# visit=[[False]*n]*n

visit=[[False]*n for _ in range(n)]
dx = [1,0]
dy = [0,1]

queue = deque([[0,0]])
flag=False
while queue:
    x,y=queue.popleft()
    cnt = board[x][y]
    if cnt==-1:
        flag=True
        break
    for i in range(2):
        nx=x+dx[i]*cnt
        ny=y+dy[i]*cnt
        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue
        if(visit[nx][ny]):
            continue
        queue.append([nx, ny])
        visit[nx][ny] = True
if flag:
    print("HaruHaru")
else:
    print("Hing")
