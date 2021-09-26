a,b = map(int,input().split())

n=int(input())

fav=[]
for i in range(n):
    fav.append(int(input()))

temp=0
count = 0
min=abs(a-b)
for i in fav:
    if min > abs(b-i):
        count=1
        min=abs(b-i)
print(count+min)
