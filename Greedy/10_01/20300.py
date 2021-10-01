import sys
n=int(input())
loss=list(map(int,sys.stdin.readline().split()))

left=0
maximum=0

loss.sort()

if len(loss)%2==1:
    left=loss.pop()

rev_loss=list(reversed(loss))

for i in range(len(loss)):
    lost=rev_loss[i]+loss[i]
    if maximum<lost:
        maximum=lost


print(max(left,maximum))





