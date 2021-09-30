import sys
n=int(input())
slime=list(map(int,sys.stdin.readline().split()))
slime.sort()
point=0
temp=0
while(len(slime)!=1):
    a=slime.pop()
    b=slime.pop()
    point+=a*b
    temp=a+b
    slime.append(temp)
    slime.sort
print(point)