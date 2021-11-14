import sys
input=sys.stdin.readline
t= int(input())
for _ in range(t):
    n=int(input())
    note1=sorted(list(map(int,input().split())))
    m=int(input())
    note2=list(map(int,input().split()))
    def bin(s,e,t,a):
        while(s<=e):
            m = (s + e) // 2
            if a[m]==t:
                return 1
            if t<=a[m]:
                e=m-1
            else:
                s=m+1
        return 0

    for i in note2:
        print(bin(0,n-1,i,note1))