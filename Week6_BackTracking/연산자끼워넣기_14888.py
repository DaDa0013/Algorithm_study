import sys

N = int(input())
num = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))

minimum = 10 ** 9
maximum = -10 ** 9

def dfs(depth, total, plus, minus, multiple, divide):
    global minimum, maximum
    if depth == N:
        # 최대 최솟값 갱신
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return 
    if plus: #plus 있으면
        dfs(depth + 1, total + num[depth], plus -1, minus, multiple, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiple, divide)
    if multiple:
        dfs(depth + 1, total * num[depth], plus, minus , multiple - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiple, divide - 1)
dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)

        
        

