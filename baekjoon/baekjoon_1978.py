import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in num:
    if i == 1:
        continue
    tmp = 0 # 소수판별변수
    for j in range(2, i//2 + 1):# 절반까지만 확인해도 소수 판별 가능
        if i % j == 0: # 나눠지는 수가 있다면 
            tmp = -1 # 소수가 아닌 경우
            break
    if tmp == 0: # 소수인 경우
        ans += 1
print(ans)