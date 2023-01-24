import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
dq = deque([i for i in range(1,n+1)])
k = list(map(int, sys.stdin.readline().split()))
count = 0
for i in k:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) <= len(dq)//2:
                dq.rotate(-1)
                count += 1
            else:
                dq.rotate(1)
                count += 1
print(count)