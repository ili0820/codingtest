import sys
input= sys.stdin.readline
n=int(input())
s=1
e=n
while(s<=e):
    m=(s+e)//2
    if m*m>=n:
        e=m-1
    else:
        s=m+1
print(e+1)