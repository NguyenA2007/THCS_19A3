d = eval(input())
res = {}

for k in d:
    if d[k] > 50:
        res[k] = d[k]

print(res)
