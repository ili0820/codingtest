n=int(input())
sum=0

#     sum+=
#
# 1 9
# 2 90
# 3 21
cnt=0
cnt=len(str(n))-1
sum=0

for i in range(cnt):
    sum+=9*(10**i)*(i+1)

sum+=(n-(10**cnt)+1)*(cnt+1)
print(sum)
