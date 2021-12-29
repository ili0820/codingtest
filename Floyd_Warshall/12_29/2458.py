#Floyd Warshall pypy3로 제출해야 시간초과 안남.
import sys
input=sys.stdin.readline

n,m=map(int,input().split())

INF=int(1e9)

graph=[[INF]*n for _ in range(n)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1
for a in range(n):
    graph[a][a]=0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][k]>graph[j][i]+graph[i][k]:
                graph[j][k]=graph[j][i]+graph[i][k]
cnt=0
temp=0
for i in range(n):
    temp=0
    for j in graph:
        if 0<j[i]<INF:
            temp+=1
    sm=sum([1 for k in graph[i] if 0<k<INF])
    temp+=sm
    if temp ==n-1:
        cnt+=1
print(cnt)