import sys

n = int(input())
s = list(map(int, sys.stdin.readline().split()))

DP = [0 for _ in range(n)]
for i in range(n):
    DP[i] = s[i]
    for j in range(i):
        if s[i] > s[j]:
            DP[i] = max(DP[i], DP[j] + s[i])
            # print(DP)
            # print(f"i = {i}")

print(max(DP))
