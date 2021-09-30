word=list(input())
temp=list("UCPC")
cnt=0
for i in word:
    if i ==temp[cnt]:
        cnt+=1
    if cnt==4:
        break
if cnt==4:
    print("I love UCPC")
else:
    print("I hate UCPC")
# Union of Computer Programming Contest club contest