import sys
input=sys.stdin.readline
answer=[]
for _ in range(9):
    answer.append(int(input()))

for i in range(9):
    for j in range(i+1,9):
        if sum(answer)-answer[i]-answer[j]==100:
            n1,n2=answer[i],answer[j]
            answer.remove(n1)
            answer.remove(n2)
            break
    if len(answer)<9:
        break
for _ in sorted(answer):
    print(_)
