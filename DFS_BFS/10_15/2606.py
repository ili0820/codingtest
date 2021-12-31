# import sys
# from collections import deque
# input=sys.stdin.readline
# n=int(input())
# m=int(input())
# graph=[[]for _ in range(n+1)]
# visit=[0 for _ in range(n+1)]
#
# cnt=0
#
# for _ in range(m):
#     a,b=map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# def dfs(start):
#     global cnt
#     visit[start]=1
#     for i in graph[start]:
#         if visit[i]==0:
#             dfs(i)
#             cnt+=1
#
#
# dfs(1)
# print(cnt)

import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
m=int(input())
graph=[[]for _ in range(n+1)]
answer=[]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
answer=set()
q=deque([1])

while(q):
    now=q.popleft()
    for next_node in graph[now]:
        if next_node not in answer:
            q.append(next_node)
            answer.add(next_node)

print(len(answer)-1)

# com = int(input())
# edge = int(input())
# node = [[] for row in range(com + 1)]
# for i in range(edge):
#     a, b = map(int, input().split())
#     node[a].append(b)
#     node[b].append(a)
#
# node_dfs = []
# while True:
#     for i in node[1]:
#         # 2 5
#         print(node[1])
#         node_dfs.append(i)
#         for j in node[i]:
#             node_dfs.append(j)
#     break
# print(node_dfs)
# while 1 in node_dfs:
#     node_dfs.remove(1)
#
# print(len(set(node_dfs)))

def dfs(graph,start,connect_count):
    visited, need_visit = list(),list()
    need_visit.append(start)
    while need_visit :
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            if node not in graph:
                continue
            else:
                need_visit.extend(graph[node])
    return visited
# 1 2 / 1 3 / 5 1 / 3 4
computer = int(sys.stdin.readline()) # 1~computer까지
connect_count = int(sys.stdin.readline()) # 연결 숫자
connect = dict()

for _ in range(connect_count):
    root, node = map(int, sys.stdin.readline().split())
    if root in connect:
        connect[root].extend([node])
    else:
        connect[root]= [node]
print(connect)
count=dfs(connect,1,connect_count)
print(count)
print(len(count)-1)
