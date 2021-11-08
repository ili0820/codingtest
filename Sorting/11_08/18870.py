import sys
input=sys.stdin.readline
n=int(input())
X=list(map(int,input().split()))
temp=list(sorted(set(X)))

dic = {temp[i] : i for i in range(len(temp))}


for _ in X:
    print(dic[_],end=" ")