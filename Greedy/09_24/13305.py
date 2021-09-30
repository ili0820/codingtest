N = int(input())
road=list(map(int,input().split()))
price=list(map(int,input().split()))

sum=0
currentprice=price[0]
for i in range(len(price)-1):
   if currentprice>price[i+1]:
       sum+=currentprice*road[i]
       currentprice=price[i+1]
   else:
       sum += currentprice * road[i]
print(sum)