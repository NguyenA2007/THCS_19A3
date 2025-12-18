n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

s = 0
for i in range(n):
    s += a[i][n - 1 - i]

print(s)
