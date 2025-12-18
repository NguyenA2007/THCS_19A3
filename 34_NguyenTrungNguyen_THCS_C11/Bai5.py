a = list(map(int, input().split()))
res = []

for x in a:
    found = False
    for y in res:
        if x == y:
            found = True
            break
    if not found:
        res.append(x)

print(res)
