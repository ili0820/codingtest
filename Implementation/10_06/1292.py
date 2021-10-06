import sys
a,b=map(int,sys.stdin.readline().split())
list =[0]
i=1
while(len(list)<b+1):
    for _ in range(i):
        list.append(i)
    i+=1

print(sum(list[a:b+1]))

