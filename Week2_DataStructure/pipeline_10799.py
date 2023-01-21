import sys
s = []
c = list(sys.stdin.readline().rstrip())
r = ['' for i in range(len(c))]
ans = 0 # 최종 조각 갯수
a = [] # 조각갯수 저장
for i in range(len(c)):
    if c[i] == '(':
        s.append('(')
        r[i] = 'start'
        a.append(1)
    else:
        if r[i - 1] == 'start': # 레이저
            r[i - 1], r[i] = 'rs', 're'
            a.pop() # start로 넣었던거 빼기 (레이저 시작이었으니)
            ans += len(a) # 스택에 있는 모든 막대에 레이저로 조각 추가
        else:
            r[i] = 'end'
            tmp = a.pop()
            ans += tmp
        s.pop()
print(ans)