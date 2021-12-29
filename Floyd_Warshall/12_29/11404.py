import sys
input=sys.stdin.readline
n=int(input())
m=int(input())

INF=int(1e9)
graph=[[INF]*n for _ in range(n)]
for a in range(n):
    graph[a][a]=0
for _ in range(m):
    a,b,c=map(int,input().split())
    if graph[a-1][b-1]>c:
        graph[a-1][b-1]=c


for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])

for i in range(n):
    for j in graph[i]:
        if j==INF:
            print(0, end=" ")
        else:
            print(j,end=" ")
    print()