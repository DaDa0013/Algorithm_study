import sys
n = int(sys.stdin.readline())
s = list(map(int,sys.stdin.readline().split()))
stack = []
ans= []
for i in range(n - 1, -1, -1):
    if len(stack) == 0:
        stack.append(s[i])
        ans.append(-1)
    else:
        if stack[-1] > s[i]:
            ans.append(stack[-1])
            stack.append(s[i])
        else:
            tmp = -1
            while stack:
                stack.pop()
                if len(stack) == 0:
                    break
                if s[i] < stack[-1]:
                    tmp = stack[-1]
                    break
            stack.append(s[i])
            ans.append(tmp)
ans = list(reversed(ans))
print(' '.join(map(str, ans)))