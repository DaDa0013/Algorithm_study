import sys

T = int(input())

def dfs(start):
    global visited
    visited[start] = True
    stack = [start]
    while stack:
        current = stack.pop()
        next = graph[current]
        if not visited[int(next)]:
            visited[next] = True
            stack.append(next)

for i in range(T):
    N = int(input())
    count = 0
    graph = [0] + list(map(int,sys.stdin.readline().split()))
    # print(graph)
    visited = [False] * (N + 1)
    for i in range(1, N + 1):
        if not visited[i]:
            count += 1
            dfs(i)
    print(count)