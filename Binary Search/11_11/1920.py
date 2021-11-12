import sys
input=sys.stdin.readline


# def binary_search(array,target,start,end):
#     if start>end:
#         return 0
#     mid = (start+end)//2
#     if array[mid]==target:
#         return 1
#     elif array[mid]>target:
#         return binary_search(array,target,start,mid-1)
#     else:
#         return binary_search(array,target,mid+1,end)
def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return 1
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return 0

n=int(input())
array=sorted(list(map(int,input().split())))
m=int(input())
numbs=list(map(int,input().split()))


for N in numbs:
    print(binary_search(array,N,0,n-1))

