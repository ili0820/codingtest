sentence=input()
find=input()
cnt=0

i=0
while i<=len(sentence) - len(find):
    if sentence[i:i+len(find)]==find:
        cnt+=1
        i+=len(find)
    else:
        i+=1
print(cnt)