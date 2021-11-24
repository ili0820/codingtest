import sys
input=sys.stdin.readline
n,m=map(int,input().split())

d=[[0 for _ in range(n)] for _ in range(m)]
dx=[1,0,1]
dy=[0,1,1]
d[0][0]=1
for i in range(m):
    d[i][0]=1
for i in range(n):
    d[0][i]=1
for j in range(1,m):
    for i in range(1,n):

        d[j][i]=d[j-1][i]+d[j][i-1]+d[j-1][i-1]

print(d[m-1][n-1]%1000000007)
#
# 1 0 0
# 0 0 0
#
# 1 1 0
# 1 0 0
#
# 1 1 1
# 1 3 5
