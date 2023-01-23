import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque([i for i in range(1, n + 1)])
count = 0
while len(q) != 1:
    if count % 2 == 0:
        q.popleft()
    else:
        q.append(q.popleft())
    count += 1
print(q[0])