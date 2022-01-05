import sys
input=sys.stdin.readline
n=int(input())
numbs=list(map(int,input().split()))
# d=numbs
# for i in range(1,n):
#     d[i]=max(d[i],d[i-1]+d[i])
# print(d)
# print(max(d))

for i in range(n):
    if i==0:
        continue
    numbs[i]=max(numbs[i],numbs[i-1]+numbs[i])
print(max(numbs))

