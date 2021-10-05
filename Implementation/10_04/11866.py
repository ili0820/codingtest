import sys


n,k=map(int,sys.stdin.readline().split())
ppl=[i for i in range(1,n+1)]
cnt=0
answer=[]
while ppl:
    if cnt!=k-1:
        ppl.append(ppl.pop(0))
        cnt+=1
    else:
        answer.append(ppl.pop(0))
        cnt=0

print("<"+ ", ".join(map(str,answer)) +">")
## deque 버전 약 50ms 정도 빠르다.  queue로 사용 할때 빠르다.
#하지만 RANDOM ACCESS 시 시간 복잡도가 O(N)이다.
#링크드 리스트 처럼 구조가 되어있기 때문에 N 번째 데이터를 접근하기 위해선 N번 iteration 필요
#list는 랜덤 엑세스에 최적화 되어있음.
#list insert pop 은 O(N)
#dqueue append pop 은 O(1)
from collections import deque
queue=deque()
queue=deque([i for i in range(1,n+1)])

while(queue):
    if cnt!=k-1:
        queue.append(queue.popleft())
        cnt+=1
    else:
        answer.append(queue.popleft())
        cnt=0
print("<"+ ", ".join(map(str,answer)) +">")