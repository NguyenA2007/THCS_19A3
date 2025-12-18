a = list(map(int, input().split()))
chan = 0
le = 0

for x in a:
    if x % 2 == 0:
        chan += x
    else:
        le += x

print(chan, le)
