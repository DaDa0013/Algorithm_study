while True:
    pw = input()
    m = ['a', 'e', 'i', 'o', 'u']

    if pw == 'end':
        break
    pw = list(pw)
    check = False
    #### 1. 모음 포함
    for i in m:
        if i in pw:
            check = True
            break
    if check == False:
        print(f'<{"".join(pw)}> is not acceptable.')
        continue
    ##### 2. 3개연속 여부
    for i in range(len(pw) - 2):
        window = pw[i:i + 3]
        m_count = 0
        for i in m:
            m_count += window.count(i)
        if m_count == 3 or m_count == 0:
            check = False
            break
    if check == False:
        print(f'<{"".join(pw)}> is not acceptable.')
        continue
    ### 3. 같은 글자 연속 여부
    for i in range(len(pw) - 1):
        if pw[i] == pw[i + 1] and pw[i] != 'e' and pw[i] != 'o':
            check = False
            break
    if check == False:
        print(f'<{"".join(pw)}> is not acceptable.')
    else:
        print(f'<{"".join(pw)}> is acceptable.')