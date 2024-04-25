N = int(input())
grid = [list(input()) for _ in range(N)]
def split_grid(a, b, l):
    first = grid[a][b]
    tmp = ''
    for i in range(a, a + l):
        for j in range(b, b + l):
            if grid[i][j] != first:
                l //= 2
                tmp += "("
                tmp += split_grid(a, b, l)
                tmp += split_grid(a, b + l, l)
                tmp += split_grid(a+l, b, l)
                tmp += split_grid(a + l, b + l, l)
                tmp += ")"

                return tmp
    return tmp + first

print(split_grid(0, 0, N))



