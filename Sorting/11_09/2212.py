import sys

input=sys.stdin.readline

n=int(input())
k=int(input())
sensors=sorted(list(map(int,input().split())))

dif=[]
for i in range(n-1):
    dif.append(sensors[i+1]-sensors[i])


print(sum(sorted(dif)[:n-k]))