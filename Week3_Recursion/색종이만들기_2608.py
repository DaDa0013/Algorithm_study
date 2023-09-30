import sys
n = int(sys.stdin.readline())
#p = [[0 for i in range(n)] for i in range(n)]
p = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
#print(p)

w = 0
b = 0
def paper(x, y, n):
    global w, b
    color = p[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if p[i][j] != color:
                paper(x, y, n//2)
                paper(x+n//2, y, n//2)
                paper(x, y+n//2, n//2)
                paper(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        w += 1
    else:
        b += 1
paper(0,0, n)
print(w)
print(b)
