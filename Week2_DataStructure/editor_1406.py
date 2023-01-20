import sys

sl = list(sys.stdin.readline().rstrip())
sr = []
for i in range(int(sys.stdin.readline())):
    tmp = sys.stdin.readline().rstrip().split()
    if tmp[0] == 'L':
        try:
            sr.append(sl.pop())
        except:
            pass
    elif tmp[0] == 'D':
        try:
            sl.append(sr.pop())
        except:
            pass
    elif tmp[0] == 'B':
        try:
            sl.pop()
        except:
            pass
    else:
        sl.append(tmp[1])

print(''.join(sl)+ (''.join(reversed(sr))))