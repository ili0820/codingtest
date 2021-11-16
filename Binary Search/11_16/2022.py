import sys
input = sys.stdin.readline
x,y,c=map(float,input().split())
s=0
e=min(x,y)
while(e-s>1e-6):
    m=(s+e)/2

    h1=(x**2-m**2)**0.5
    h2=(y**2-m**2)**0.5
    temp=(h1*h2)/(h1+h2)
    if temp<c:
        e=m
    else:
        s=m
print("{:.3f}".format(m))
