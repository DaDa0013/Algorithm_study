import sys
from collections import deque
def Y(n,k):
    l = []
    dq = deque([i for i in range(1,n+1)])
    while True:
        if len(dq) == 1:
            l.append(dq.popleft())
            break
        else:
            for i in range(k-1):
                dq.rotate(-1)
            l.append(dq.popleft())
    return l
n, k = map(int, sys.stdin.readline().split())
ans = Y(n,k)
print('<', end = '')
for i in range(len(ans) - 1):
    print(ans[i], end = ', ')
print(ans[-1], end= '')
print('>')