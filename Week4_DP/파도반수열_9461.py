def padoban(n):
    dp = [1, 1, 1, 2, 2, 3]
    if n <= 6:
        print(dp[n-1])
    else:
        for i in range(6, n):
            dp.append(dp[i-1] + dp[i - 5])
        print(dp[-1])
t = int(input())
for i in range(t):
    n = int(input())
    padoban(n)