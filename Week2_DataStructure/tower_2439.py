import sys
from collections import deque
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
ans = []
m = [] # (n, index)
for i in range(n):
    if m:
        if m[-1][0] < s[i]:
            while True:
                m.pop()
                if len(m) == 0:
                    m.append([s[i], i + 1])
                    ans.append(0)
                    break
                elif m[-1][0] > s[i]:
                    ans.append(m[-1][1])
                    m.append([s[i], i + 1])
                    break
        else:
            ans.append(m[-1][1])
            m.append([s[i], i + 1])
    else:
        ans.append(0)
        m.append([s[i], i + 1])
print(' '.join(map(str,ans)))