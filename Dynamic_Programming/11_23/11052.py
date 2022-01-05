import sys
input=sys.stdin.readline
n=int(input())
prices=list(map(int,input().split()))
d=[0]*(n+1)

for i in range(1,n+1):
    for j in range(1,i+1):
        d[i]=max(d[i-j]+prices[j-1],d[i])

print(d[n])

# d[0]+prices[2] or d[1]+prices[1]
#
# d[0]+prices[3] or d[1]+prices[2] or d[2]+prices[1]
#
# d[0]+prices[4] or d[1]+prices[3] or d[2]+prices[2] or d[3]+prices[1]
#
# d[0]+prices[5] or d[1]+prices[4] or d[2]+prices[3] or d[3]+prices[2] or d[4]+prices[1]
#