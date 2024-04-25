# from collections import deque
N = int(input())
gaps = list(map(int, input().split()))
people = [i for i in range(1, N + 1)]
answer = [N]
for i in range(N - 1, 0, -1): # 맨끝사람 제외 # 어차피 gap이 0임
    if len(answer) > gaps[i - 1]:
        # 끼워넣기
        answer.insert(gaps[i - 1], i)
    else:
        #뒤에 넣기
        answer.append(i)

print(*answer)