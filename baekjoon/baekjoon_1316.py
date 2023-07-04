import sys

n = int(sys.stdin.readline())
ans = 0
for i in range(n):
    tmp = []
    w = sys.stdin.readline()
    for i in w:
        if len(tmp) == 0: # 첫번째인 경우
            tmp.append(i)
        else:
            if i in tmp:
                if tmp[-1] != i: # 연속된 경우
                    tmp.append(-1)
                    break
            tmp.append(i)
    if tmp[-1] != -1:
        ans += 1
print(ans)