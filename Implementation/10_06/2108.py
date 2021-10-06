import sys
from collections import Counter

n=int(input())
numbers=[int(sys.stdin.readline().strip()) for _ in range(n)]

mean=round(sum(numbers)/n)

median=sorted(numbers)[n//2]

temp=Counter(numbers).most_common()
temp2=[]


for i in range(len(temp)):
    if temp[i][1]==temp[0][1]:
        temp2.append(temp[i])
if len(temp2)>1:
    temp2.sort()
    common=temp2[1][0]
else:
    common = temp[0][0]
rang=max(numbers)-min(numbers)

print(mean,end="\n")
print(median,end="\n")
print(common,end="\n")
print(rang)
