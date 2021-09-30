import sys
n=int(input())
votes=[int(sys.stdin.readline().strip())for i in range(n)]
me=votes.pop(0)
count=0
if votes==[]:
    count=0
else:
    votes.sort(reverse=True)
    for i,j in enumerate(votes):
        while(votes[0]>=me):
            count += 1
            votes[i] -= 1
            me += 1
            votes.sort(reverse=True)

print(count)

