m, n = map(int, input().split())
a = []

for i in range(m):
    a.append(list(map(int, input().split())))

max_sum = None
row = 0

for i in range(m):
    s = 0
    for j in range(n):
        s += a[i][j]
    if max_sum is None or s > max_sum:
        max_sum = s
        row = i

print(row)
