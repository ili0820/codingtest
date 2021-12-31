# import sys
# from collections import deque

# input=sys.stdin.readline

# a,b,n,m=map(int,input().split())

# visited=[False for _ in range(100001)]
# mov=[0 for _ in range(100001)]
# dx=[-1,1,a,b,-a,-b,a,b]


# def bfs(x):
#     queue=deque()
#     visited[x]=True
#     queue.append(x)
#     while(queue):
#         x=queue.popleft()
#         for i in range(6):
#             nx=x+dx[i]
#             if 0<=nx<100001 and not visited[nx]:
#                 queue.append(nx)
#                 visited[nx]=1
#                 mov[nx]=(mov[x]+1)
#         for i in range(1,3):
#             nx=x*dx[-i]
#             if 0<=nx<100001 and not visited[nx]:
#                 queue.append(nx)
#                 visited[nx]=1
#                 mov[nx]=(mov[x]+1)

# bfs(n)
# print(mov[m])


import sys
from collections import deque

input=sys.stdin.readline

a,b,n,m=map(int,input().split())

visited=[False for _ in range(100001)]
mov=[0 for _ in range(100001)]


def bfs(x):
    queue=deque()
    visited[x]=True
    queue.append(x)
    while(queue):
        x=queue.popleft()
        for nx in [x-1,x+1,x+a,x+b,x-a,x-b,x*a,x*b]:
            if 0<=nx<100001 and not visited[nx]:
                queue.append(nx)
                visited[nx]=1
                mov[nx]=(mov[x]+1)
            if nx==m:
                return


bfs(n)
print(mov[m])


