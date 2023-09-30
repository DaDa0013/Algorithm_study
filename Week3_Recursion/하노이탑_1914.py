
import sys
n = int(sys.stdin.readline())

# n = n번쨰 원판
# _from = 출발지
# _to = 목적지
# _else = 보조 기둥
def hanoi(num, _from, _to, _else):
    if num == 1:
        print(_from, _to)
    else:
        hanoi(num - 1, _from, _else, _to)  # 나머지를 보조기둥으로
        print(_from, _to)  # n번째 원판 옮기기
        hanoi(num - 1, _else, _to, _from)  # 나머지 원판들을 보조기둥에서 다시 목적지로

print(2**n - 1)  # 옮긴 횟수
# 항상 맨마지막 원판은 1번만 움직이고 나머지 원판은 2번씩 움직이니까 -1해주면 된다
if n <= 20:
    hanoi(n, 1, 3, 2)
