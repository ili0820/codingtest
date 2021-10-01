import sys
n=int(input())
tips=[int(sys.stdin.readline().strip()) for x in range(n)]
sum=0
tips.sort(reverse=True)

for numb,tip in enumerate(tips,start=1):
    if tip-(numb-1)>0:
        sum+=tip-(numb-1)

print(sum)