import sys
n = int(input())

size=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]


for i in range(n):
    cnt=1
    for j in size:
        if j[0]> size[i][0] and j[1]>size[i][1]:
            cnt+=1
    print(cnt,end=" ")

