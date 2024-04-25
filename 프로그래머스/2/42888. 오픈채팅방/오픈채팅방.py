def solution(record):
    answer = []
    users = {}
    for r in record:
        tmp = list(r.split(" "))
        if len(tmp) == 3:
            users[tmp[1]] = tmp[2]
    for r in record:
        tmp = r.split(" ")
        if tmp[0] == 'Enter':
            m = "님이 들어왔습니다."
        elif tmp[0] == 'Leave':
            m = "님이 나갔습니다."
        else:
            continue
        answer.append(users[tmp[1]] + m)

    return answer