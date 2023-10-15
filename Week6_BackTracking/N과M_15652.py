import sys
n, m = map(int, sys.stdin.readline().split())

s = []
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        # print(i)
        # print(s)
        if len(s) != 0 and i >= s[-1]:
            s.append(i)
            dfs()
            s.pop()
        elif len(s)== 0:
            s.append(i)
            dfs()
            s.pop()
dfs()