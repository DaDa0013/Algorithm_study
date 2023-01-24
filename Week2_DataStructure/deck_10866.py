import sys
from collections import deque
q = deque()
for i in range(int(sys.stdin.readline())):
    m = sys.stdin.readline().split()
    if m[0] == 'push_front':
        q.appendleft(int(m[1]))
    elif m[0] == 'push_back':
        q.append(int(m[1]))
    elif m[0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif m[0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif m[0] == 'size':
        print(len(q))
    elif m[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif m[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)