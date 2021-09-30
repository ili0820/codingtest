a,b=map(int,input().split())
cnt=0
while(b!=a):
    if b%10%2==0:
        b/=2
        cnt+=1
    elif b%10==1:
        b//=10
        cnt+=1
    elif b%10%2==1:
        print(-1)
        break

    if b==0:
        print(-1)
        break
if a==b:
    print(cnt+1)






