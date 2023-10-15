import sys

n = int(input())
s = list(map(int, sys.stdin.readline().split()))

DP = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if s[i] < s[j]:
            DP[i] = max(DP[i], DP[j] + 1)
print(max(DP))
