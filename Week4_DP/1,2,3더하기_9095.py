def summ(n):
    dp = [1, 2, 4]
    if n <= 3:
        print(dp[n-1])
    else:
        for i in range(3, n):
            dp.append(dp[i-1] + dp[i-2] + dp[i-3])
        print(dp[n-1])


T = int(input())
for i in range(T):
    n = int(input())
    summ(n)