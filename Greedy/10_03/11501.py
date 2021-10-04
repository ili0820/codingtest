import sys
t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    n=int(input())
    prices=list(map(int,sys.stdin.readline().split()))

    sum=0
    max=0
    for i in range(len(prices)-1,-1,-1):
        if prices[i]>max:
            max=prices[i]
        else:
            sum+=max-prices[i]
    print(sum)
#1 1 3 1 5
#-1 -1 -3 -1 +20
#-1 -1 +6 -1 +5

# 3 5 9
