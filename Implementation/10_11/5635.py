import sys
n=int(input())

ppl=[]
for _ in range(n):
    name,d,m,y=sys.stdin.readline().split()
    ppl.append([name,int(d),int(m),int(y)])
ppl.sort(key=lambda x : (x[3],x[2],x[1]))

print(ppl[-1][0])
print(ppl[0][0])
