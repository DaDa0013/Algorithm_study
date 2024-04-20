from itertools import permutations
import copy
def solution(expression):
    answer = 0
    tmp = ''
    num = []
    oper = []
    
    def calculate(num, oper, current_o):
        while True:
            if current_o in oper:
                i = oper.index(current_o)
                if current_o == '*':
                    num[i] = num[i] * num[i + 1]
                elif current_o == '-':
                    num[i] =num[i] - num[i + 1]
                else:
                    num[i] =num[i] + num[i + 1]
                num.pop(i + 1)
                oper.pop(i)
            else:
                break
        return num, oper
    
    for i in expression:
        if i in ['+', '-', '*']:
            num.append(int(tmp))
            oper.append(i)
            tmp = '' 
        else:
            tmp += i
    
    num.append(int(tmp))
    orders = []
    for i in permutations(list(set(oper)), len((set(oper)))):
        orders.append(i)
    
    print(orders)
    
    for order in orders:
        t_num = copy.deepcopy(num)
        t_oper = copy.deepcopy(oper)
        for o in order:
            t_num, t_oper = calculate(t_num, t_oper, o)
            
        answer = max(answer, abs(t_num[0]))
    
    
    return answer