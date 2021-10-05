# #소수 판별해서 하기
# import sys
# n,k=map(int,sys.stdin.readline().split())
#
# numbers=[x for x in range(2,n+1)]
#
# def isprime(a):
#     i = 2
#     while i * i <= a:
#         if a % i == 0:
#             return False
#         i += 1
#     return True
#
# answer=[]
#
# while(len(answer)!=len(numbers)):
#     for i in numbers:
#         if isprime(i):
#             answer.append(i)
#             for j in numbers[i:]:
#                 if j%i==0 and  j not in answer:
#                     answer.append(j)
#
# print(answer[k-1])


#소수 판별 없이 하기
import sys
n,k=map(int,sys.stdin.readline().split())

answer=[]

for i in range(2,n+1):
    if i not in answer:
        answer.append(i)
    for j in range(i,n+1):
        if j%i==0 and  j not in answer:
            answer.append(j)

print(answer[k-1])

#배열을 만들어 방문 했는지 확인 후 안했으면 했다고 표시후 cnt 늘려서 세기
import sys
n,k=map(int,sys.stdin.readline().split())

answer=[0]*n
cnt=0
for i in range(2,n+1):
    if answer[i-1]==0:
        for j in range(i,n+1,i):
            if answer[j-1]==0:
                answer[j-1]=1
                cnt+=1
            if cnt==k:
                print(j)
                break
