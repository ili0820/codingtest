import sys
n=int(input())
S=[]
def add(S,x):
    if x not in S:
        S.append(x)
    return

def rem(S,x):
    if x in S:
        S.remove(x)
    return
def check(S,x):
    if x in S:
        print(1)
    else:
        print(0)
    return
def toggle(S,x):
    if x in S:
        S.remove(x)
    else:
        S.append(x)
    return

for _ in range(n):
    command=sys.stdin.readline().split()
    if command[0]=="add":
        add(S,int(command[1]))
    elif command[0]=="remove":
        rem(S,int(command[1]))
    elif command[0]=="check":
        check(S,int(command[1]))
    elif command[0]=="toggle":
        toggle(S,int(command[1]))
    elif command[0]=="all":
        S = [x for x in range(1, 21)]
    elif command[0]=="empty":
        S = []