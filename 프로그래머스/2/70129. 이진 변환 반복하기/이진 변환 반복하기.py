from collections import Counter
def solution(s):
    answer = []
    count, c_cnt = 0, 0
    
    def change(s):
        nonlocal count
        # print(Counter(s))
        count += Counter(s)['0']
        n = len(s.replace('0',''))
        n = bin(n)
        return n
    
    while True:
        s = change(s)
        c_cnt += 1
        if len(str(s)) == 3: # 0b1
            break
        else:
            s = s[2:]    
    return [c_cnt, count]