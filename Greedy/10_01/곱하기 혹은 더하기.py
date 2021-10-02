import sys
s = list(map(int,sys.stdin.readline().rstrip()))
print(s)
sum=s[0]
for i in s[1:]:
    if sum<=1 or i<=1:
        sum+=i
    else:
        sum*=i

print(sum)

