import sys
n=int(input())
files=[sys.stdin.readline().strip() for _ in range(n)]

answer=list(files[0])

for i in range(1,n):
    for j in range(len(files[0])):
        if answer[j]!=files[i][j]:
            answer[j]="?"

print("".join(answer))
