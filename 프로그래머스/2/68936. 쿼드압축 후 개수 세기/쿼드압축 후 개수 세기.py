from collections import Counter
def solution(arr):
    answer = [0, 0] # 0, 1
    
    ## 사각형 분할
    def divide_square(s_arr):
        l = len(s_arr)
        k = l // 2
        square = [[],[],[],[]]
        ###### 한칸-> 한개인경우
        if k == 1:
            i = 0
            for si in s_arr:
                for s in si:
                    square[i].append(s)
                    i += 1
            return square
        #### 아닌경우
        square = [[row[:k] for row in s_arr[:k]], [row[k:] for row in s_arr[:k]], [row[k:] for row in s_arr[k:]], [row[:k] for row in s_arr[k:]]]
        ##### square = [[1번째줄], [2번째줄], [3번째줄], [4번째줄]]
        return square 
    
    ### 갯수 확인
    def count_square(s_arr):
        nonlocal answer
        ########### 종료 조건1 => 한줄에 한개인 경우 (다 나눠짐)
        if len(s_arr[0]) == 1:
            for si in s_arr:
                if si == [0]:
                    answer[0] += 1
                else:
                    answer[1] += 1
            return
        
        for si in s_arr:
            tmp_answer = [0, 0]
            l = len(si)
            for i in si:
                c = Counter(i)
                tmp_answer[0] += c[0]
                tmp_answer[1] += c[1]
            ######## 2-1. 모두 0 or 1 인 배열 => answer 배열 업데이트 & stop
            if l ** 2 in tmp_answer:
                if tmp_answer[0] == l ** 2:
                    answer[0] += 1 
                else:
                    answer[1] += 1
            else:
            ######## 2-2. 아닌 경우 =>  배열 4개  [[],[],[],[]] divide_squre() 재귀
                count_square(divide_square(si))

                
    ####### 처음에 다 1 or 0 인 경우(예외)
    n = arr[0]
    check = True
    for s in arr:
        if n != s:
            check = False
            break
    if check:
        if n[0] == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    else:
        count_square(divide_square(arr))
    return answer