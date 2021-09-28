n=int(input())
arrival=[]
for i in range(n):
   arrival.append(list(map(int,input().split())))
arrival.sort()
current_time=0
for i,j in arrival:
   if current_time<i:
       current_time=i
   current_time+=j

print(current_time)

