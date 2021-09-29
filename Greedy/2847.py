n=int(input())
m=[]
for i in range(n):
    m.append(int(input()))
m.reverse()
count=0
current=m[0]
for i in range(len(m)-1):
    while(m[i]<=m[i+1]):
        count+=1
        m[i+1]-=1
print(count)