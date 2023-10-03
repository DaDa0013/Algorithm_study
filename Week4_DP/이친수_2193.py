import sys
n = int(sys.stdin.readline())
dp = [[0, 0] for _ in range(n + 1)]
# dp[i][j] = i자리 이친수 갯수  , j = j로 끝나는 이친수 개수 (j = 0, 1)
dp[0][1] = 1
dp[1][0] = 1
if n <= 2:
    print(1)
else:
    for i in range(2, n):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]
    print(dp[n-1][0] + dp[n-1][1])