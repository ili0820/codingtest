import sys
n=int(input())
fear=list(map(int,sys.stdin.readline().split()))
fear.sort(reverse=True)
cnt=0
while(fear):
    temp=[]
    temp.append(fear.pop(0))
    number =temp[0]
    while(number!=len(temp)):
        temp.append(fear.pop(0))
    cnt+=1

print(cnt)

