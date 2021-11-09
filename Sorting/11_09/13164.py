import sys
input=sys.stdin.readline
n,k=map(int,input().split())

numbs=list(map(int,input().split()))

dif=[]
for i in range(n-1):
    dif.append(numbs[i+1]-numbs[i])


print(sum(sorted(dif,reverse=True)[k-1:]))
#print(sum(sorted(dif)[:n-k]))

