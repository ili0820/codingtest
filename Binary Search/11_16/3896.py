import sys
input=sys.stdin.readline
t=int(input())

array=[False,False]+[True]*1299710
primes=[]
for i in range(2,1299710):
    if array[i]:
        primes.append(i)
        for j in range(i+i,1299710,i):
            array[j]=False
print(array)
for _ in range(t):
    k=int(input())
    if k in primes:
        print(0)
    else:
        s=0
        e=100000
        while(s<=e):
            m=(s+e)//2
            if k<=primes[m-1]:
                e=m-1
            else:
                s=m+1

        print(primes[s-1]-primes[e-1])
