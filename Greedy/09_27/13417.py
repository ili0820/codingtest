t=int(input())
final=[]
for i in range(t):
    n=int(input())
    card=list(input().split())

    answer=[]
    answer.append(card.pop(0))

    for i in card:
        if answer[0] >= i:
            answer.insert(0,i)
        else:
            answer.append(i)
    answer="".join(answer)
    final.append(answer)

for i in final:
    print(i)


