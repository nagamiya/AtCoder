n, m = map(int, input().split())
h = list(map(int, input().split()))
ab = [map(int, input().split()) for _ in range(m)]
a, b = [list(i) for i in zip(*ab)]
ans = [1] * n
for i in range(m):
    if (h[a[i] - 1] == h[b[i] - 1]):
        ans[a[i] - 1] = 0
        ans[b[i] - 1] = 0
    elif (h[a[i] - 1] > h[b[i] - 1]):
        ans[b[i] - 1] = 0
    else:
        ans[a[i] - 1] = 0

result = sum(i == 1 for i in ans)
print(result)

#1 1 1 1 1 1
#0 1 1 1 1 1
#0 1 1 0 1 1
