t = tuple(map(int, input().split()))
chan = []
le = []
s1 = 0
s2 = 0

for x in t:
    if x % 2 == 0:
        chan.append(x)
        s1 += x
    else:
        le.append(x)
        s2 += x

print(tuple(chan), s1)
print(tuple(le), s2)
