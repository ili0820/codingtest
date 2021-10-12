import sys
n,m=map(int,sys.stdin.readline().split())

castle=[list(sys.stdin.readline().strip()) for _ in range(n)]
row,col=n,m

for i in range(n):
    if "X" in castle[i]:
        row-=1
for j in range(m):
    if "X" in [castle[i][j]for i in range(n)]:
            col-=1

print(max(col,row))

