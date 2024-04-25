
import sys
input = sys.stdin.readline
N, M, L, K = map(int, input().split())
pos = [tuple(map(int, input().split())) for _ in range(K)] # 별똥별 좌표들
ans = 0 

for fx, fy in pos: # 별똥별 한개
    for sx, sy in pos: # 또 다른 별똥별

        stars = 0
        for px, py in pos: 
            if fx <= px <= fx + L and sy <= py <= sy + L: stars += 1
        ans = max(ans, stars) # 튕겨진 최대 별똥별 갯수 
print(K - ans)