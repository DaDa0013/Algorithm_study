import sys
N = int(input())
matrix = []
print(matrix)

for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
print(matrix)