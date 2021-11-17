import sys
input=sys.stdin.readline
n,m=map(int,input().split())
s=sorted([input().strip() for _ in range(n)])
corpus=sorted([input().strip() for _ in range(m)])
cnt=0
idx=0
for test in corpus:
    for i in range(idx,len(s)):
        if s[i].startswith(test):
            cnt+=1
            idx=i
            break
print(cnt)