import sys
n=int(input())
price=[int(sys.stdin.readline().strip())for i in range(n)]
total=0
price.sort(reverse=True)
if len(price)<3:
    total=sum(price)
elif len(price)>=3:
    for i in range(len(price)):
        if (i+1)%3!=0:
            total+=price[i]

print(total)