import sys
T = int(input())
for _ in range(T):
    n = int(input())
    total_s = 0
    stickers = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    DP = [[0 for _ in range(n)] for _ in range(3)] # DP[0 or 1][j] = 해당값 넣고 최댓값, 2 => 현재값 안넣음 최대
    DP[0][0], DP[1][0], DP[2][0]= stickers[0][0], stickers[1][0], 0
    for i in range(1, n):
        DP[0][i] = max(DP[1][i - 1],  DP[2][i - 1]) + stickers[0][i]
        DP[1][i] = max(DP[0][i - 1], DP[2][i - 1]) + stickers[1][i]
        DP[2][i] = max(DP[0][i - 1], DP[1][i - 1])
    print(max(DP[0][-1], DP[1][-1],DP[2][-1]))