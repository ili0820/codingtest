import sys
n=int(input())
t=list(map(int,sys.stdin.readline().split()))
t.sort(reverse=True)
days=0
for i, j in enumerate(t,start=1):
    days = max(days, i+j)

print(days+1)