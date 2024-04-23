T = int(input())

for t in range(T):
    N = int(input())
    tree = {}

    for _ in range(N - 1):
        a, b = map(int, (input().split()))
        if b in tree:
            tree[b].append(a)
        else:
            tree[b] = [a]
    n1, n2 = map(int, (input().split())) # a, b의 공통 조상 구하자
    parent1, parent2 = [n1],[n2]


    while True:
        if n1 in tree.keys():
            # print(tree[n1])
            parent1.append(tree[n1][0])
            n1 = tree[n1][0]
        else:
            break
    # print(parent1)
    while True:
        if n2 in tree.keys():
            parent2.append(tree[n2][0])
            n2 = tree[n2][0]
        else:
            break

    for i in parent1:
        if i in parent2:
            print(i)
            break
# print(parent1, parent2)



