import sys

n = int(sys.stdin.readline())
for i in range(n):
    s = []
    tmp = sys.stdin.readline().strip()
    for j in tmp:
        if j == '(':
            s.append('(')
        else:
            try:
                s.pop()
            except:
                print('NO')
                break
    else:
        if s:
            print('NO')
        else:
            print('YES')