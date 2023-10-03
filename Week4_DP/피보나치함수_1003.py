
def fibo(t):
    z = [1, 0]
    o = [0, 1]
    if t >= 2:
        for i in range(1, t): #아래서부터 올라가기
            z.append(z[i-1] + z[i])
            o.append(o[i-1] + o[i])
    print(z[t], o[t])

n = int(input())
for i in range(n):
    t = int(input())
    fibo(t)
