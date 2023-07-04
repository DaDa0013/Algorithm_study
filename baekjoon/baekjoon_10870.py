import sys
n = int(sys.stdin.readline())
f = [0, 1]
for i in range(2, n+1):
    ans = f[i-1] + f[i-2]
    f.append(ans)
print(f[-1])