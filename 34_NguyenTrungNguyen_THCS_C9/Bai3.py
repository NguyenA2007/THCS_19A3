def kiem_tra_so_armstrong(n):
    s = sum(int(d)**3 for d in str(n))
    return s == n
