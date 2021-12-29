import sys
n=int(input())

INF=int(1e9)
graph=[[INF]*n for _ in range(n)]

for a in range(n):
    graph[a][a]=0

while(True):
    temp=list(map(int,input().split()))
    if temp ==[-1,-1]:
        break

    graph[temp[0]-1][temp[1]-1]=1
    graph[temp[1] - 1][temp[0] - 1] = 1


for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])

answer=[]
print(graph)
for _ in graph:
    answer.append(max(_))

print(min(answer),answer.count(min(answer)))
temp = [i for i, value in enumerate(answer) if value == min(answer)]
for _ in temp:
    print(_+1,end=" ")

