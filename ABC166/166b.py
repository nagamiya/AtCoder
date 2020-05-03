import itertools

n, k = map(int, input().split())
a = []
sunuke = list(range(1, n + 1))

# 標準入力わからん
for i in range(k):
    d = int(input())
    a.append(map(int, input().split()))

a2 = list(itertools.chain.from_iterable(a))
result = set(sunuke) - set(a2)
print(len(result))