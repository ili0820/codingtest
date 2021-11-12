import sys
input=sys.stdin.readline
n=int(input())
requests=sorted(list(map(int,input().split())))
M=int(input())

s=0
e=max(requests)
while(s<=e):
    m=(s+e)//2

    price = sum([i for i in requests if i <= m]) + sum( [m for i in requests if i >m])
    print(m,price)
    if price <= M:
        s = m + 1
    else:
        e = m - 1
print(e)
