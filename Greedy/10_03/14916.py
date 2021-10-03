n=int(input())
if n ==3 or n==1:
    print(-1)
else:
    fives=n//5
    n-=(fives*5)
    while(n%2!=0):
        fives-=1
        n+=5
    twos=n//2
    print(twos+fives)

