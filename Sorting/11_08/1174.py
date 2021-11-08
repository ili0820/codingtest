import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):

    n=int(input())

    dic={}
    for x,y in [list(map(int,input().split())) for _ in range(n)]:
        if x not in dic:
            dic[x]=[]
        dic[x].append(y)
    dic=sorted(dic.items())
    current=[0,0]
    min=100000
    answer=[]
    for i in dic:
        x=i[0]
        i[1].sort(key=lambda x :abs(x-current[1]))
        for _ in range(len(i[1])):
            y=i[1][_]
            answer.append([x,y])
        current[0]=x
        current[1]=y

    caffes=list(map(int,input().split()))
    for idx in caffes[1:]:
        print(answer[idx-1][0],answer[idx-1][1])
