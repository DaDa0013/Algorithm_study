N = int(input())
pattern = input()
s = pattern.index('*')
prev = pattern[:s]
suf = pattern[s+1:]
files = [list(input()) for _ in range(N)]
for file in files:
    if len(file) >= len(prev) + len(suf):
        check = 'DA'
        for i in range(len(prev)): # * 앞
            if file[i] != prev[i]:
                check = 'NE'
                break
        if check == 'DA':
            for i in range(-1, -len(suf) - 1, -1):  # * 뒤
                if file[i] != pattern[i]:
                    check = 'NE'
                    break
        print(check)
    else:
        print('NE')