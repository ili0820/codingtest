import sys
INF=int(1e9)
input=sys.stdin.readline
n=int(input())
graph=[[INF]*(n) for _ in range(n)]


for _ in range(n):
        graph[_]=list(map(int,input().split()))

for a in range(n):
    for b in range(n):
        if graph[a][b]==0:
            graph[a][b]=INF


for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(n):
    for b in range(n ):
        if graph[a][b]==INF:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()