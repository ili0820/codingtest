import sys
a,p=map(int,sys.stdin.readline().split())
numbers=[a]
while(True):
    temp=0
    for s in str(numbers[-1]):
        temp+=int(s) ** p
    if temp in numbers:
        break
    numbers.append(temp)

print(numbers.index(temp))