from itertools import permutations
n = int(input())
k = int(input())
numbers = [input() for _ in range(n)]
nums = []
for i in permutations(numbers, k):
    nums.append(''.join(i))
print(len(set(nums)))