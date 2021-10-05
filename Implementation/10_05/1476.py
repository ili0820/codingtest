import sys
target=list(map(int,sys.stdin.readline().split()))
e,s,m=1,1,1
cnt=1
while True:
    if e==target[0] and s==target[1] and m==target[2]:
        print(cnt)
        break
    e+=1
    if e==16:
        e=1

    s+=1
    if s==29:
        s=1

    m += 1
    if m==20:
        m=1
    cnt+=1


