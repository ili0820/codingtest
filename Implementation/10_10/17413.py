import sys
s=sys.stdin.readline().strip()
temp=[]
answer=[]
counter=0
for  i in s:
    if i=="<":
        answer.append(reversed(temp))
        temp = []
        counter=1
        temp.append(i)


    elif i ==">":
        counter=0
        temp.append(i)
        answer.append(temp)
        temp=[]
    elif i == " " and counter ==0 :
        answer.append(list(reversed(temp)))
        answer.append(" ")
        temp=[]
    else:
        temp.append(i)

answer.append(list(reversed(temp)))
for _ in answer:
    print("".join(_),end="")

#####################
import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":       # 열린 괄호를 만나면
        i += 1
        while word[i] != ">":      # 닫힌 괄호를 만날 때 까지
            i += 1
        i += 1               # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i+=1
        tmp = word[start:i] # 숫자,알파벳 범위에 있는 것들을
        tmp.reverse()       # 뒤집는다
        word[start:i] = tmp
    else:                   # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i+=1                # 그냥 증가시킨다

print("".join(word))

#https://hongcoding.tistory.com/62