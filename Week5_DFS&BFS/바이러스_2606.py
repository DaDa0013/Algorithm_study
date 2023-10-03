import sys

n = int(input())
v = int(input()) #간선 수

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
count = 0

def dfs(start):
    global count
    visited[start] = True
    stack = [start]
    while stack:
        current = stack.pop()
        for i in graph[current]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                count += 1

for i in range(v):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)
print(count)
