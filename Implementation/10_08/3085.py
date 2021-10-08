import sys
n=int(input())
board=[list(sys.stdin.readline().strip())for _ in range(n)]

maximum=1

def count(n,board):
    maximum=1
    # 가로 행
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if board[i][j]==board[i][j+1]:
                cnt+=1
            else:
                cnt=1

            if cnt>maximum:
                maximum=cnt
    # 세로 열
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if board[j][i]==board[j+1][i]:
                cnt+=1
            else:
                cnt=1
            if cnt>maximum:
                maximum=cnt
    return maximum
#가로 행
for i in range(n):

    for j in range(n-1):
        # temp=board[i][j]
        # board[i][j]=board[i][j+1]
        # board[i][j + 1]=temp
        # maximum=max(maximum,count(n,board))
        # temp = board[i][j]
        # board[i][j]=board[i][j+1]
        # board[i][j + 1]=temp
        board[i][j],board[i][j+1]=board[i][j+1],board[i][j]
        maximum=max(maximum,count(n,board))
        board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
#세로 열
for i in range(n):
    for j in range(n-1):
        # temp=board[j][i]
        # board[j][i]=board[j+1][i]
        # board[j+1][i]=temp
        # maximum=max(maximum,count(n,board))
        # temp=board[j][i]
        # board[j][i]=board[j+1][i]
        # board[j+1][i]=temp
        board[j][i],board[j+1][i]=board[j+1][i],board[j][i]
        maximum=max(maximum,count(n,board))
        board[j][i],board[j+1][i]=board[j+1][i],board[j][i]

print(maximum)
