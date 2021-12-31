import sys
read=sys.stdin.readline
n,m=map(int,read().split())

graph=[]
for i in range(n):
    graph.append(list(read().strip()))
visit=[[False]*m for _ in range(n)]
print(graph,visit)
cnt=0
def dfs(x,y):
    global cnt
    now=graph[x][y]
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return
    if visit[x][y]==False:
        visit[x][y]=True
        if visit[x][y]!=now:
            cnt+=1

