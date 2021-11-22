import sys
input=sys.stdin.readline


# def cal(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 2
#     elif n==3:
#         return 4
#     else:
#         return cal(n-1)+cal(n-2)+cal(n-3)
# t=int(input())
# for _ in range(t):
#     n=int(input())
#     print(cal(n))

d=[0]*11
d[1]=1
d[2]=2
d[3]=4
for i in range(4,11):
    d[i]=d[i-1]+d[i-2]+d[i-3]
t=int(input())
for _ in range(t):
    n=int(input())
    print(d[n])