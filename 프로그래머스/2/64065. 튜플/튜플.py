from collections import Counter
def solution(s):
    answer = []
    n = ''
    for i in range(1, len(s)):
        if s[i] != '{' and s[i] != '}':
            n += s[i]
    
    n_count = Counter(list(n.split(',')))
    n_count = Counter.most_common(n_count)
    for i in n_count:
        # print(i[0])
        answer.append(int(i[0]))

    return answer
