import sys
sys.setrecursionlimit(10**7) # 제귀제한 넓히기

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0

def dfs(start):
    # print(f'count = {count}')
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            dfs(i)
    return # 다 True인 경우

for i in range(1, N+1):
    if visited[i] == False:
        count += 1 # 한 사이클 끝남
        dfs(i)
        
print(count)            