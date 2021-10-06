import sys
import itertools
from collections import Counter
n=int(input())
places=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
answer=[[0 for _ in range(101)] for _ in range(101)]

for x,y in places:
    for i in range(10):
        for j in range(10):
            answer[x+j][y+i]=1

cnt=list(itertools.chain(*answer))
print(Counter(cnt)[1])

#itertools 쓰는게 더느리다!
N = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

answer = 0
for row in paper:
    answer += row.count(1)
print(answer)