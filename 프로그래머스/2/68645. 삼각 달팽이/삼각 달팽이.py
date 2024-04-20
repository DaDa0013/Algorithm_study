from collections import deque
def solution(n):
    k = n * (n + 1) // 2
    
    def snail():
        cursor, current, r = 0, 1, n
        answer = [[[],[],deque([])] for i in range(n)] # [up][right][down]
        while r > 0:
            ### down
            # print(f'down')
            for _ in range(r):
                answer[cursor][0].append(current)
                # print(f'cursor = {cursor}')
                # print(f'current = {current}')
                # print('--------')
                current += 1
                cursor += 1
            r -= 1
            ### right
            # print(f'right')
            cursor -= 1
            if r > 0:
                for _ in range(r):
                    answer[cursor][1].append(current)
                    # print(f'cursor = {cursor}')
                    # print(f'current = {current}')
                    # print('--------')
                    current += 1
            else:
                return answer
            ### up
            # print(f'up')
            r -= 1
            cursor -= 1
            if r > 0:
                for _ in range(r):
                    answer[cursor][2].appendleft(current)
                    # print(f'cursor = {cursor}')
                    # print(f'current = {current}')
                    # print('--------')
                    current += 1
                    cursor -= 1
            else:
                return answer    
            r -= 1
            cursor += 2
        return answer
    
    answer = snail()
    tmp = []
    
    for i in answer:
        for j in i:
            if len(j) != 0:
                tmp += j
    # print(tmp)
    
    return tmp