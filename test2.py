import sys
def cal(bigger,smaller,answer):
    i=1
    while(smaller*i<=bigger):
        answer.append(smaller*i)
        i += 1

    i=1
    while (bigger - smaller * i>0):
        answer.append(bigger - smaller * i)
        i += 1

def solution(l1, l2):
    answer=[]
    answer.append(l1)
    answer.append(l2)
    bigger=max(l1,l2)
    smaller=min(l1,l2)
    cal(bigger,smaller,answer)
    temp=answer[-1]
    new_b=bigger-(smaller-temp)
    while(new_b not in answer and new_b >0):
        answer.append(new_b)
        cal(new_b,smaller,answer)
        temp = answer[-1]
        new_b  =bigger- (smaller - temp)
    answer=sorted(list(set(answer)))
    return answer





l1=22
l2=100

print(solution(l1,l2))
# 0 0
# 0 30
# 4 26
# 4 22
# 4 18
# 4 14
# 4 10
# 4 6
# 4 2
# 2 0

# 0 0
# 0 4
# 4 8
# 4 12
# 4 16
# 4 20
# 4 24
# 4 28

#11 30

#11 0
#11 11
#11 22

#22 100
#0 0
#0 22
#0 44
#0 66
#0 88
#0 100
#0 78
#0 56
#0 34
#0 12
#12 0
#22 90
#0  68
#0 46
#0 24
#0 2
#2 98
# 8 3
# 0 0
# 3 0
# 6 0
# 8 0
# 5 0
# 2 0
# 0 2
# 8 2
# 7 3
# 4 0
# 1 0
