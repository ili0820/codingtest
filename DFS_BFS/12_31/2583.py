import sys
from collections import deque

input=sys.stdin.readline

m,n,k=map(int,input().split())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
graph=[[0]*(n) for _ in range(m)]


rect=[]
for _ in range(k):
    rect.append(list(map(int,input().split())))

for x1,y1,x2,y2 in rect:

    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[j][i]=1


"""
0 0 0 0 1 1 0
0 1 0 0 1 1 0
1 1 1 1 0 0 0
1 1 1 1 0 0 0
0 1 0 0 0 0 0
"""
"""
0 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0
1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0
0 1 1 0 1 1 1 0
0 0 0 0 1 1 1 0
"""
def bfs(y,x,temp):

    queue=deque()
    graph[y][x]=1
    queue.append((y,x))
    while(queue):
        y,x=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[ny][nx]==0:
                graph[ny][nx]=1
                queue.append((ny,nx))
                temp+=1
    return temp
    

cnt=[]
for y in range(m):
    for x in range(n):
        if graph[y][x]==0:
            temp=1
            cnt.append(bfs(y,x,temp))
print(len(cnt))

for i in sorted(cnt):
    print(i,end=" ")
