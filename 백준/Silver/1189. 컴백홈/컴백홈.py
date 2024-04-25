r, c, k = map(int, input().split())
grid = [list(input()) for _ in range(r)]
# print(grid)
answer = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[False for _ in range(c)] for _ in range(r)]

def dfs(current, depth, visited):
    global grid, r, c, k, dx, dy, answer
    visited[current[0] - 1][current[1] - 1] = True
    if depth > k:
        return
    if current == (1, c) and depth == k:
        answer += 1
        return
    for i in range(4):
        nx, ny = current[0] + dx[i], current[1] + dy[i]
        if 1 <= nx <= r and 1 <= ny <= c and grid[nx - 1][ny - 1] == '.' and visited[nx - 1][ny - 1] == False:
            visited[nx - 1][ny - 1] = True
            dfs((nx, ny), depth + 1, visited)
            visited[nx - 1][ny - 1] = False
    return
dfs((r , 1), 1, visited)
print(answer)