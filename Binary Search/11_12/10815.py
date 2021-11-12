import sys
input=sys.stdin.readline

n=int(input())
numbs=sorted(list(map(int,input().split())))
m=int(input())
tests=list(map(int,input().split()))

def binary(s,e,t,a):
    while(s<=e):
        m = (s + e) // 2
        if a[m] == t:
            return 1
        elif t<a[m]:
            e=m-1
        else:
            s=m+1
    return 0

for t in tests:
    print(binary(0,n-1,t,numbs),end=" ")
