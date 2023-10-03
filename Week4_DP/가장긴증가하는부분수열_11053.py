import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))

stack = []
stack.append(A[0])
for i in A:
    if i > stack[-1]:
        stack.append(i)
print(len(stack))