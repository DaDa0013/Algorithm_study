N, M = map(int, input().split())
robot = list(map(int, input().split())) # r, c, d(=방향) (상, 우, 하, 좌)
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)]for _ in range(N)]
def dfs(robot):
    global grid, N, M, visited
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    stack = [robot]
    answer = 0
    while stack:
        check = False
        x, y, d = stack.pop()
        if visited[x][y] == False:
            answer += 1
            visited[x][y] = True
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0 and visited[nx][ny] == False:
                d = (d + 3) % 4 # 반시계 회전
                check = True
                break
        if check == True: # 상하좌우 청소 안한 칸 있음
            nx, ny = dx[d] + x, dy[d] + y
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0 and visited[nx][ny] == False:
                stack.append([nx, ny, d])
            else:
                stack.append([x, y, d])
        else: # 청소 안한 칸 없음
            nx, ny = dx[(d + 2) % 4] + x, dy[(d + 2) % 4] + y# 후진
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0: # 후진 가능
                stack.append([nx, ny, d])
    return answer
print(dfs(robot))