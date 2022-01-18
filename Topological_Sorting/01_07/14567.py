import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
indegree=[0]*(n+1)
graph=[[] for i in range(n+1)]
time=[1 for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topological_sort():
    q=deque()

    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        now=q.popleft()
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
                time[i]=time[now]+1


topological_sort()

for i in time[1:]:
    print(i,end=" ")