a = list(map(int, input().split()))
k = int(input())

n = len(a)
k = k % n
res = []

for i in range(n):
    if i < k:
        res.append(a[n - k + i])
    else:
        res.append(a[i - k])

print(res)
