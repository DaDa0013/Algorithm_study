import sys
from collections import deque

def printer(n, m, dq):
    count = 0
    while True:
        if m == 0:
            if dq.index(max(dq)) == 0:
                dq.popleft()
                count += 1
                break
            else:
                dq.rotate(-1)
                m += (len(dq)-1)
        else:
            if dq[0] == max(dq):
                dq.popleft()
                count += 1
                m -= 1
            else:
                dq.rotate(-1)
                m -= 1
    return count
t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    dq = deque(sys.stdin.readline().split())
    print(printer(n, m, dq))