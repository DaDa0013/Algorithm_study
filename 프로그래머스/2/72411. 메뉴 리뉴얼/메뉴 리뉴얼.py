from itertools import combinations
def solution(orders, course):
    answer = []
    for cl in course:
        order_dict = {}
        for order in orders:
            tmp_order = list(order)
            for c in combinations(tmp_order, cl):
                o = ''.join(sorted(c))
                if o in order_dict:
                    order_dict[o] += 1
                else:
                    order_dict[o] = 1
        
        if len(order_dict) != 0 and max(order_dict.values()) >= 2:
            max_order = [k for k,v in order_dict.items() if max(order_dict.values()) == v]
            print(max_order)  
            print(max(order_dict, key = order_dict.get))
            for m in max_order:
                answer.append(m)
    answer.sort()
    return answer