import sys
n=int(input())
numbers= [sys.stdin.readline().strip() for _ in range(n)]
print(numbers)
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for alp in numbers:
    print(alp)
    if alp in ALPHABET:
        print(ALPHABET.index(alp))
# GCF + ACDEB
# 876
# 97543
#
# 98654
# 783
#
# 9864
#  785
#
#  98753
#  00684
#
# 9
# 8