# BT5.py - Tính S1..S4
import math

def S1(n):
    return n*(n+1)//2

def S2(n):
    # 1*2*...*(n-1)
    if n <= 1:
        return 1
    prod = 1
    for i in range(1, n):
        prod *= i
    return prod

def S3(n):
    s = 0.0
    for i in range(1, n+1):
        s += ((-1)**(i+1)) * (1.0/i)
    return s

def S4(n):
    s = 0.0
    for k in range(0, n+1):
        s += k / (k + 2)
    return s

if __name__ == "__main__":
    n = int(input("Nhập n (số nguyên dương): ").strip())
    print("S1 =", S1(n))
    print("S2 =", S2(n))
    print("S3 =", S3(n))
    print("S4 =", S4(n))
