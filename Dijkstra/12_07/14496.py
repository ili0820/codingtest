import sys
import heapq
from collections import deque
input=sys.stdin.readline
INF=int(1e9)


a,b=map(int,input().split())
n,m=map(int,input().split())
graph=[[]for _ in range (n+1)]
distance=[INF]*(n+1)
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append((y,1))
    graph[y].append((x, 1))

def dijkstra(start):
        q=[]
        heapq.heappush(q,(0,start))
        distance[start]=0
        while q:
            dist,now=heapq.heappop(q)
            if distance[now]<dist:
                continue
            for i in graph[now]:
                cost=dist+i[1]
                if cost < distance[i[0]]:
                    distance[i[0]]=cost
                    heapq.heappush(q,(cost,i[0]))
dijkstra(a)
print(-1 if distance[b]==INF else distance[b])

