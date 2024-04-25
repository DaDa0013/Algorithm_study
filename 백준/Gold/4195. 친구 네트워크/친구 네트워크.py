
T = int(input())
def find(target): # 루트 부모 찾기
    if target == parent[target]:# 자기자신의 부모
        return target
    else:
        parent[target] = find(parent[target]) # 루트 부모 최신화
        return parent[target]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y: # 루트 부모 같음
        return
    else:
        # 부모노드 다름
        parent[y] = x # y의 부모 = x
        visited[x] += visited[y] # x가 부모인 그룹의 크기 업데이트(x에 y 그룹 다 추가)

for _ in range(T):
    F = int(input())
    parent = {}
    visited = {} # visited[a] = a가 루트 부모인 그룹의 크기
    for _ in range(F):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            visited[a] = 1
        if b not in parent:
            parent[b] = b
            visited[b] = 1

        union(a,b)
        # print(visited)
        print(visited[find(a)])