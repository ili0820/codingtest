import sys
input=sys.stdin.readline
n=int(input())
times=[]
for _ in range(n):
    times.append(list(map(int,input().split())))
times=sorted(times,key=lambda x : -x[1])

print(times)
t,s=times.pop(0)
time= s-t

while times:
    t, s = times.pop(0)
    if time > s:
        time=s-t
    else:
        time-=t

print(time if time >=0 else -1)

# 0 1 2
# 20<1+ 8 + 3
# 16< 8 + 3

