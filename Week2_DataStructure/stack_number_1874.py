import sys
s = []
ans = ''
n = 1
for i in range(int(sys.stdin.readline())):
    t = int(sys.stdin.readline())
    while n <= t:
        s.append(n)
        n += 1
        ans += '+'
    if t != s[-1]:
        ans = 'NO'
        break
    else:
        ans += '-'
        s.pop()
if ans == 'NO':
    print(ans)
else:
    for i in ans:
        print(i)