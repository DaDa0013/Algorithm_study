import sys
from collections import deque
N, M, V = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M): # 해당 인덱스(노드)에 연결된 노드 추가
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    visited[start] = True
    print(start, end = ' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(i)
def bfs(start):
    queue = deque([start])
    visited[start] = True
    print(start, end = ' ')

    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


# 정렬 (작은 순부터)
for i in graph:
    i.sort()

# dfs
visited = [False] * (N + 1)
dfs(V)
print()

# bfs
visited = [False] * (N + 1)
bfs(V)





# graph = [[False] * (N + 1) for _ in range(N + 1)]

# for _ in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a][b] = True
#     graph[b][a] = True

# visited_d = [False] * (N + 1)
# visited_b = [False] * (N + 1)

# def bfs(V): # 그래프이기 때문에 bfs는 순차탐색
#     q = deque([V]) # 탐색할 정점을 넣은 큐 생성
#     visited_b[V] = True # 해당 V 노드 방문 함
#     while q: # q가 빌때까지
#         V = q.popleft() # 큐 첫번째값 (왼쪽 우선)
#         print(V, end = ' ')
#         for i in range(1, N + 1): # 정점 번호가 작은거부터 우선 방문해야함
#             if not visited_b[i] and graph[V][i]: # i노드 방문 X & V와 연결되어있는 경우
#                 q.append(i)
#                 visited_b[i] = True

# def dfs(V): # 
#     visited_d[V] = True#해당 V 방문
#     print(V, end = " ")
#     for i in range(1, N + 1):
#         if not visited_d[i] and graph[V][i]: # i노드 방문 X & V와 연결되어있는 경우
#             dfs(i) # 해당 값으로 더 깊이 들어감

# dfs(V)
# print()
# bfs(V)
