import sys
k = int(input())
money=[]
temp = [int(sys.stdin.readline().strip()) for _ in range(k)]
for _ in temp:
    if _==0:
        money.pop()
    else:
        money.append(_)
print(sum(money))