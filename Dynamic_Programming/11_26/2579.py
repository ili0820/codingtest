import sys
input=sys.stdin.readline
n=int(input())
stairs=[ int(input()) for _ in range(n)]

stairs.append(0)
stairs.append(0)
d=[0]*(n+2)

d[1]=stairs[0]
d[2]=stairs[0]+stairs[1]

#d[3]=max(stairs[1]+stairs[2],stairs[0]+stairs[2])
#d[4]=max(stairs[0]+stairs[2]+stairs[3],stairs[0]+stairs[1]+stairs[3])
for i in range(3,n+1):
   d[i]=max(d[i-3]+stairs[i-2]+stairs[i-1],d[i-2]+stairs[i-1])
    # d[i]=max(d[i-1]+stairs[i-1],d[i-2]+stairs[i-1])
print(d[n])

