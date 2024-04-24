import sys
sys.setrecursionlimit(1000000)
n, m = map(int, sys.stdin.readline().split())
s = [i for i in range(n + 1)] # 자기 자신을 부모로 가짐
def find_p(x):
    if s[x] != x: # 자기자신 아니라면 이미 나의 부모가 있음
        s[x] = find_p(s[x])
    return s[x]

def union(a, b):
    a = find_p(a) # a의 부모
    b = find_p(b) # b의 부모
    if a < b:
        s[b] = a # b의 부모는 a
    else:
        s[a] = b # a의 부모는 b


for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().split())
    if c == 0:
        union(a, b)
        # print(a, b, s)
    else:
       if find_p(a) == find_p(b): # 같은 부모
           print("YES")
       else:
           print("NO")

