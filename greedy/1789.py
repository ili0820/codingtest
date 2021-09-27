s=int(input())
n=0
while(s>n):
    s-=n
    n += 1
    if n>s:
        n-=1
        break
print(n)

