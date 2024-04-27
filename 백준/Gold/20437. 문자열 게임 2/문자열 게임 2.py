from collections import Counter
import copy
T = int(input())
for t in range(T):
    word = list(input())
    k = int(input())
    ###### k 개 이상인 문자들의 각 인덱스 배열 생성
    #### idx['a'] = [a의 인덱스들]
    w_count = Counter(word)
    idx = {}
    for w in w_count:
        if w_count[w] >= k:
            for i in range(len(word)):
                if word[i] == w:
                    idx[w] = idx.get(w, []) + [i] # 이미 인덱스 들어있으면 그 뒤에 이어붙여라 / 없으면 [] + [i]
    if len(idx) == 0:
        print(-1)
        continue
    # print(idx)

    min_len, max_len = len(word), -1
    for key, value in idx.items():
        for i in range(len(value) - k + 1):
            min_len = min(min_len, value[i + k - 1] - value[i] + 1) # k개 포함하는 문자열 길이
            max_len = max(max_len, value[i + k - 1] - value[i] + 1)

    print(min_len, max_len)