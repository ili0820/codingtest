import sys
input=sys.stdin.readline
n=int(input())
array=[float(input().rstrip()) for _ in range(n)]
print(array)
d=[0]*(n+1)
for i in range(1,n):
    array[i]=max(array[i-1]*array[i],array[i])
print("{:.3f}".format(max(array)))
