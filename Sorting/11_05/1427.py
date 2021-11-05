import sys

n=sys.stdin.readline().rstrip()
print("".join(sorted(n,reverse=True)))