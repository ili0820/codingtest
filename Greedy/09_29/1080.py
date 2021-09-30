n,m=list(map(int,input().split()))
a=[]
b=[]

for i in range(n):
    a.append(list(map(int,input())))
for i in range(n):
    b.append(list(map(int,input())))

def swap(i,j,c):
    for x in range(i,i+c):
        for y in range(j,j+c):
            a[x][y] = 1 - a[x][y]
count =0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j]!=b[i][j]:
                swap(i,j,3)
                count+=1
if a != b:
    count=-1

print(count)

# 1110
# 1100
# 1110
#
#
# 0000
# 0010
# 0000
#
# 1001
# 1011
# 1001

1001
1011
1001