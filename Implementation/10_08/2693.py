import sys
n=int(input())
for _ in range(n):
    array=list(map(int,sys.stdin.readline().split()))
    array.sort(reverse=True)
    print(array[2])
