from collections import deque

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:

        v=queue.popleft()
        print(v, end="")
        for i in graph[v]:
            if not visited[i] and i!=-1:
                queue.append(i)
                visited[i] = True

def solution(nest, n):
    answer = -1

    visited=[False]*len(nest)
    bfs(nest,0,visited)
    return answer


nest=[[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
n=3
solution(nest,n)