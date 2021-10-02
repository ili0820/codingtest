import sys
n,k=map(int,input().split())
time=[int(sys.stdin.readline().strip()) for x in range(n)]
dif=[]
for i in range(n-1):
    dif.append(time[i+1]-time[i]-1)

dif.sort()
print(n+sum(dif[:n-k]))

# #
# # 5
# # 1 2 5 6 8 11 13 15 16 20
# #  1 3 1 2 3 2 2 1 4
# #  1 1 1 2 2 2 3 3 4
# #1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
# #1 1 0 0 1 1 0 1 0 0 1 0 1 0 1 1 1
# #1 1 0 0 1 1 0 1 0 0 1 1 1 0 1 1 1




# input = __import__('sys').stdin.readline
#
# n, k = map(int,input().split())
# t = [int(input()) for i in range(n)]
# empty = sorted(t[i+1]-t[i]-1 for i in range(n-1))
# print(empty)
# print(empty[:n-k])
# print(n + sum(empty[:n-k]))