answer =[]
while(1):
    n=[i for i in input().split()]
    count=int(n.pop(0))
    if count==0:
        break
    n.sort()
    s=n.count('0')
    for i in range(s):
        n.remove('0')
    b = []
    a = []
    a=n[0::2]
    b=n[1::2]
    while(s):
        if len(a)<=len(b):
            a.insert(1,'0')
            s-=1
        elif len(a)>=len(b):
            if s!=0:
                b.insert(1,'0')
                s-=1
            else:
                break
    a=''.join(a)
    b=''.join(b)
    a = int(a)
    b = int(b)
    answer.append(a+b)

for i in answer:
    print(i)



#9 0 1 2 3 4 0 1 2 3

#pop(0)
#0 1 2 3 4 0 1 2 3

#sort()
#0 0 1 1 2 2 3 3 4

#remove('0')
#1 1 2 2 3 3 4

#a=n[0::2]
#b=n[1::2]
#1 2 3 4
#1 2 3


#1 2 3 4
#1 0 0 2 3


