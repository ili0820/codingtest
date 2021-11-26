import sys

input=sys.stdin.readline
n=int(input())
d=[0]*(n+4)
d[0]=1

for i in range(1,n+1):
    for j in range(i):
        d[i]+=(d[j]*d[i-j-1])

print(d[n])


# 0 * n-1
# 1 * n-2
# 2 * n-3
#
# 2-2 2-0
# 2-1 2-1
# 2-0 2-2
#
# 1-1 1-0
# 1-0 1-1