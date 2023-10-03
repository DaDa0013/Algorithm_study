def r(n):
    dp = [1, 2, 3]
    if n <= 3:
        print(dp[n-1] % 10007)
    else:
        for i in range(3, n):
            dp.append(dp[i-1] + dp[i-2])
        print(dp[n-1] % 10007)    

n = int(input())
r(n)