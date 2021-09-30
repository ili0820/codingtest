T=int(input())
n=[]
for i in range(T):
    n.append(int(input()))

fibonacci=[0,1]
cnt = 0
while(fibonacci[-1]<max(n)):
    fibonacci.append((fibonacci[cnt]+fibonacci[cnt+1]))
    cnt += 1

fibonacci.sort(reverse=True)
fibonacci.remove(0)

for number in n:
    left=number
    answer=[]
    for i in range(len(fibonacci)):
        if left >= fibonacci[i]:
            left-=fibonacci[i]
            answer.append(fibonacci[i])
    answer.sort()
    for b in range(len(answer)):
        print(answer[b], end=' ')




