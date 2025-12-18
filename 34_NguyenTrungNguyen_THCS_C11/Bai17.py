d = eval(input())
mk = None
mv = None

for k in d:
    if mv is None or d[k] > mv:
        mv = d[k]
        mk = k

print(mk)
