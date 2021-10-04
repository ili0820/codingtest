import sys
t=int(input())
for _ in range(t):
    n,loc=map(int,sys.stdin.readline().split())
    priority=list(map(int,sys.stdin.readline().split()))
    sequence=list(enumerate(priority))
    cnt=0
    while True:
        if sequence[0][1]==max(sequence,key=lambda x:x[1])[1]:
            cnt+=1
            if sequence[0][0]==loc:
                print(cnt)
                break
            else:
                sequence.pop(0)
        else:
            sequence.append(sequence.pop(0))


# 0,1
# 1,1
# 2,9
# 3,1
# 4,1
# 5,1
#
# 2,9
# 3,1
# 4,1
# 5,1
# 0,1
# 1,1

