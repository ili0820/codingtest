import sys
input=sys.stdin.readline
graph=[]
tmp=[[0]*5 for _ in range(5)]
for _ in range(5):
    graph.append(list(map(int,input().split())))

bingo=[]
for _ in range(5):
    bingo.append(list(map(int,input().split())))

cnt=0
total=0

def check(temp):
    cnt=0
    for x in range(5):
        if sum(temp[x])==5:
            cnt+=1
        if sum([k[x] for k in temp])==5:
            cnt+=1
    if temp[0][0]+temp[1][1]+temp[2][2]+temp[3][3]+temp[4][4]==5:
        cnt+=1
    if temp[0][4]+temp[1][3]+temp[2][2]+temp[3][1]+temp[4][0]==5:
        cnt+=1
    return cnt

cnt=0
def check2():
    cnt=0
    for i in range(5):
        for j in bingo[i]:
            for k in range(5):
                if j in graph[k]:
                    tmp[k][graph[k].index(j)]=1
                    cnt+=1
                    if check(tmp)>=3:
                        return cnt
cnt=check2()


print(cnt)



