s = input("Nhập chuỗi: ")

res = ""
i = 0
while i < len(s):
    if s[i] != " ":
        res += s[i]
    else:
        if res != "" and res[-1] != " ":
            res += " "
    i += 1

if res and res[-1] == " ":
    res = res[:-1]

print(res)
