m, n = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]

p, q = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(p)]

if n != p:
    print("Khong nhan duoc")
else:
    C = [[0]*q for _ in range(m)]
    for i in range(m):
        for j in range(q):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    for r in C:
        print(r)
