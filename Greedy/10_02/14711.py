import sys
n=int(input())
top=list(sys.stdin.readline().rstrip())

for i in range(n):
    if top[i] =="#":
        top[i]=1
    else:
        top[i]=0
top=[top]

for _ in range(n-1):
    top.append([0 for _ in range(n)])
print(top)

array=[[0 for _ in range(n)]]*n
print(array)
for y in range(n):
    for x in range(n):
        if top[y][x]==1:
            array[y][x]+=1
            if y-1>=0:
                array[y - 1][x] += 1
            if y+1<=n-1:
                array[y + 1][x] += 1
            if x - 1 >= 0:
                array[y][x-1] += 1
            if x + 1 <= n-1:
                array[y][x+1] += 1
        for i in range(n):
            print(array[i][::])
        print()

for y in range(n):
    for x in range(n):
        if top[y][x]%2==0:
            top[y][x]=1
        else:
            top[y][x]=0

print(top)
#
# 010
# 000
# 000

#FAILED