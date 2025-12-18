a = list(map(int, input().split()))
k = int(input())

n = len(a)
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == k:
            print(a[i], a[j])
