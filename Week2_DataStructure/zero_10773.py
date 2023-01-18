import sys
n = int(sys.stdin.readline())
s = []
for i in range(n):
    tmp = int(sys.stdin.readline().strip())
    if tmp == 0:
        s.pop()
    else:
        s.append(tmp)
print(sum(s))