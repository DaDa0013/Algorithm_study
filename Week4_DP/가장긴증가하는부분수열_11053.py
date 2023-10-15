import sys

n = int(input())
s = list(map(int, sys.stdin.readline().split()))

DP = [1 for i in range(n)]
for i in range(n):
    for j in range(n):
        if s[i] > s[j] and DP[i] <= DP[j]:
            DP[i] = DP[j] + 1
print(max(DP))
