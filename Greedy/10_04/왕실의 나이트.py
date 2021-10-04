loc=input()
n=8
x,y= map(int,(ord(loc[0])-ord("a")+1,loc[1]))
cnt=0
# x+2,y-1
# x+2,y+1
if x+2<n:
    if y-1>1:
        cnt+=1
    if y+1<n:
        cnt+=1
# x - 2, y - 1
# x - 2, y + 1
if 1<x-2:
    if y-1>1:
        cnt+=1
    if y+1<n:
        cnt+=1
# x-1,y-2
# x-1,y+2
if 1<x-1:
    if y-2>1:
        cnt+=1
    if y+2<n:
        cnt+=1
# x+1,y-2
# x+1,y+2
if x+1<n:
    if y-2>1:
        cnt+=1
    if y+2<n:
        cnt+=1
print(cnt)

