import sys
n, m = map(int, sys.stdin.readline().split())
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n+1):
        if i not in s:
            if len(s) != 0 and i > s[-1]: # 들어있는 경우는 오름차순으로만
                s.append(i)
                dfs()
                s.pop()
            elif len(s) == 0: # 0인경우는 넣어주기
                s.append(i)
                dfs()
                s.pop()         

dfs()