import copy
def solution(s):
    answer = 10 ** 7
    start = s[0]
    s_count = [0]
    s = list(s)
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):
        count = 0
        tmp_s = ''
        stack = s[:i]

        for j in range(i, len(s), i):
            tmp = s[j:j + i]
            if stack == tmp:
                # print(stack)
                count += 1
                # print(stack, tmp, count)
            else:
                if count > 0:
                    # print(stack, tmp, count)
                    tmp_s += (str(count + 1) + ''.join(stack))
                    # print((str(count + 1) + ''.join(stack)))
                else:
                    tmp_s += ''.join(stack)
                stack = tmp
                count = 0
        if count > 0:
            tmp_s += (str(count + 1) + ''.join(stack))
        else:
            tmp_s += ''.join(stack)
        # print(tmp_s)
        answer = min(answer, len(tmp_s))
                
    return answer