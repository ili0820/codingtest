import sys
import statistics as st
input=sys.stdin.readline
n,m=map(int,input().split())
board=[list(map(int,input().split())) for i in range(m)]
board=sorted(board)
Xs=[board[x][0] for x in range(m)]
Ys=[board[x][1] for x in range(m)]
X=sorted(Xs)[m//2]
Y=sorted(Ys)[m//2]
#기본 라이브러리 사용.
# X=int(st.median([board[x][0] for x in range(m)]))
# Y=int(st.median([board[x][1] for x in range(m)]))
cnt=0
for x,y in board:
    cnt+=(abs(X-x)+abs(Y-y))
print(cnt)