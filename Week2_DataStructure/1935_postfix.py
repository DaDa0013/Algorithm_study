import sys

n = int(sys.stdin.readline())
s = []
num = []
p = sys.stdin.readline().strip()
for i in range(n):
    num.append(int(sys.stdin.readline()))
for i in p:
    if i not in ['+', '-', '*', '/']:
        s.append(num[ord(i) - ord('A')])
    else:
        a = s.pop()
        b = s.pop()
        if i == '+':
            s.append(a + b)
        elif i == '-':
            s.append(b - a)
        elif i == '*':
            s.append(a * b)
        elif i == '/':
            s.append(b / a)
        else:
            pass
print(f'{s.pop():.2f}')