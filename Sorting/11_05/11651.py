import sys
input=sys.stdin.readline

n=int(input())
answer=[]
for _ in range(n):
    answer.append(list(map(int,input().split())))
# answer=sorted(answer,key= lambda x : x[0])
# answer=sorted(answer,key= lambda x : x[1])

answer=sorted(answer,key= lambda x : (x[1],x[0]))

for x,y in answer:
    print(x,y)