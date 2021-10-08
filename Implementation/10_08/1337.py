import sys
n=int(input())
numbers=[int(sys.stdin.readline().strip()) for _ in range(n)]
numbers.sort()
maximum=0

for i in range(n):
    cnt=0
    array=[numbers[i]+j for j in range(5)]
    k=0
    while(i+k<n):
        if numbers[i+k] in array:
            cnt+=1
        k+=1
    if cnt>maximum:
        maximum=cnt

print(5-maximum)

