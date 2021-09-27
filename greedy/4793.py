answer=[]
while(1):
    L,P,V=list(map(int,input().split()))
    if L ==0:
        break
    else:
        cnt=V//P*L
        if V%P<L:
            cnt+=V%P
        else:
            cnt+=L
        answer.append(cnt)

for i,j in enumerate(answer):
    print("Case {0}: {1}".format(i+1,j))



