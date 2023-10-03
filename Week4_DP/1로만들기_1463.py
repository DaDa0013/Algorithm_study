# count = 0
# def makeone(n):
#     global count  
#     if n == 1:
#         print(count)
#     else:
#         if (n % 2) * (n % 3) == 0:
#             if n % 3 == 0:
#                 count += 1
#                 makeone(n//3)
#             elif n % 2 == 0:
#                 count += 1
#                 makeone(n//2)
#         else:
#             makeone(n-1)
    
# n = int(input())
# makeone(n)

n = int(input())
dp = [0] * (n + 1)

for i in range(2, n + 1): # 거슬러 올라가기 
    dp[i] = dp[i - 1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])