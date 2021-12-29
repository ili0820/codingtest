import sys

input=sys.stdin.readline
INF=int(1e9)

n=int(input())

graph=[[INF]*(n) for _ in range(n)]


for _ in range(n-1):
    k=int(input())
    temp=list(map(int,input().split()))

    for __ in range(k):

        graph[_][temp[__]-1] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

def func(n,graph):
    for a in range(n):
            if 0<graph[0][a]<INF:
                if 0 < graph[a][a]<INF:
                    return 1
    return 0

print("CYCLE" if func(n,graph) else "NO CYCLE")

