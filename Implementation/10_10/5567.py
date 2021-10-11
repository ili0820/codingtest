import sys
n= int(input())
m= int(input())
relationship=dict()
for i in range(1,n+1):
    relationship[i]=[]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    relationship[a].append(b)
    relationship[b].append(a)
answer=set(relationship[1])
for i in relationship[1]:
    answer.update(relationship[i])
if len(answer)!=0:
    print(len(answer)-1)
else:
    print(len(answer))

# 5
# 3
# 1 3
# 2 4
# 1 2
# [2, 3]
# 5