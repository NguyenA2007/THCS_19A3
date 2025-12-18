A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_B = []
B_A = []
G = []

for x in A:
    if x not in B:
        A_B.append(x)

for x in B:
    if x not in A:
        B_A.append(x)

for x in A:
    if x in B:
        G.append(x)

print(A_B)
print(B_A)
print(G)
