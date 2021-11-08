import sys
from collections import Counter

def solution(lottos):
    lottos=" ".join(lottos)
    bonus=[]
    for _ in range(len(lottos)):
        if lottos[_] == "(":
            start=_
        if lottos[_]==")":
            bonus.append(lottos[start:_+1])

    for _ in bonus:
        lottos=lottos.replace(_,"")
    lottos=lottos.replace("  "," ").split()

    bonus="".join(bonus)
    bonus = bonus.replace("(", "")
    bonus = bonus.replace(")", " ").rstrip().split()

    B_counter=sorted(Counter(bonus).most_common(),key= lambda x:(x[1],-int(x[0])),reverse=True)[:6]
    L_counter=sorted(Counter(lottos).most_common(),key= lambda x:(x[1],-int(x[0])),reverse=True)[:6]
    answer=[]
    for key,numbers in L_counter:
        answer.append(int(key))
    temp=0
    for key,numbers in B_counter:
        if int(key) not in answer:
            answer.append(int(key))
            temp=key
            break
    if temp == 0:
        temp=sorted(list(map(int,bonus)))[0]+1
        answer.append(temp)
    print(temp)
    answer=sorted(answer)

    f=[]
    print(answer)
    for _ in answer:
        if _ ==int(temp):
            f.append("("+str(_)+")")
        else:
            f.append(_)
    print(f)
    answer="".join(str(f)).replace("[","").replace("]","").replace("'","").replace(",","")


    return answer

lottos=["15 10 39 5 1 21 (22)", "11 5 (10) 39 1 8 44", "(39) 10 5 22 15 9 20", "22 10 5 1 (15) 3 2", "10 (5) 22 1 15 41 38", "10 5 39 33 17 14 (1)"]
result="5 12 15 (17) 18 20 23"


solution(lottos)