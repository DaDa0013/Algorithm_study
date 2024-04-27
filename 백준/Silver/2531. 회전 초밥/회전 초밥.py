from collections import Counter
n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]
belt += belt[:k]
max_s = 0
for i in range(n):
    tmp = belt[i:i+k] + [c]
    max_s = max(len(set(tmp)), max_s)
print(max_s)