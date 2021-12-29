import sys
input=sys.stdin.readline
INF=int(1e9)
t= int(input())

for _ in range(t):
    n=int(input())
    graph = [[INF] * (n+2) for _ in range(n+2)]
    temp=[list(map(int,input().split())) for _ in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            if i== j:
                continue
            dist=abs(temp[i][0]-temp[j][0]) + abs(temp[i][1]-temp[j][1])
            if dist<=1000:
                graph[i][j]=1

    for k in range(n+2):
        for a in range(n+2):
            for b in range(n+2):
                #min 보다 빠르다!
                if graph[a][b]> graph[a][k]+graph[k][b]:
                    graph[a][b]=graph[a][k]+graph[k][b]


    print("happy" if 0<graph[0][-1]<INF else "sad")
