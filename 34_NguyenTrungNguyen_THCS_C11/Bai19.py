d = eval(input())
res = {}

for name in d:
    score = d[name]
    if score not in res:
        res[score] = [name]
    else:
        res[score].append(name)

print(res)
