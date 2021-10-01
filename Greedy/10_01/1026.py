import sys
n=int(input())
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))
a.sort()
b.sort(reverse=True)
sum=0
for i, j in zip(a,b):
    sum+=i*j
print(sum)