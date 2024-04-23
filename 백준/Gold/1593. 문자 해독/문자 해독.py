g, s = map(int, input().split())
W = input()
S = input()

answer = 0
wa = [0] * 58  # word의 문자 배열
sa = [0] * 58  # S의 문자 배열
for i in W:
    wa[ord(i) - 65] += 1
start, length = 0, 0

for i in range(s):
    sa[ord(S[i]) - 65] += 1  # 해당 문자 표기
    length += 1

    if length == g:  # 비교할 문자열과 길이 동일
        if wa == sa:
            answer += 1
        sa[ord(S[start]) - 65] -= 1  # 슬라이딩 윈도우 -> 방금 넣었던것 뺴기
        start += 1  # 문자열 처음 위치 옮기기
        length -= 1
print(answer)
# https://velog.io/@dhelee/%EB%B0%B1%EC%A4%80-1593%EB%B2%88-%EB%AC%B8%EC%9E%90-%ED%95%B4%EB%8F%85-Python-%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%94%A9-%EC%9C%88%EB%8F%84%EC%9A%B0