import sys

n = int(sys.stdin.readline())
s = []
for i in range(n):
    tmp = sys.stdin.readline().split()
    if tmp[0] == 'push':
        s.append(int(tmp[1]))
    elif tmp[0] == 'pop':
        try:
            print(s.pop())
        except:
            print(-1)

    elif tmp[0] == 'size':
        print(len(s))
    elif tmp[0] == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif tmp[0] == 'top':
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])
    else:
        print('잘못 입력하셨습니다')