from collections import Counter
n=input()
sn=0

for _ in n:
    if _ =="6"or _=="9":
        sn+=1
if sn%2==0:
        sn=sn//2
else:
        sn=sn//2+1

cnt=Counter(n)
del(cnt["6"])
del(cnt["9"])
cnt=cnt.most_common()
if len(cnt):
    print(max(sn,cnt[0][1]))
else:
    print(sn)
