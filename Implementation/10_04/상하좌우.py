import sys
n = int(input ())
plan=sys.stdin.readline().split()
print(plan)
x,y=1,1
for i in plan:
    if i =="R":
        if x<n:
            x+=1

    if i =="L":
        if 0<x:
            x-=1

    if i =="U":
        if 1<y:
            y-=1

    if i =="D":
        if y<n:
            y+=1

print(y,x)