# BT1.py - Kiểm tra số chính phương
import math

def is_perfect_square(n):
    if n < 0:
        return False
    r = int(math.isqrt(n))  # Python 3.8+: math.isqrt trả căn bậc hai nguyên
    return r*r == n

if __name__ == "__main__":
    try:
        n = int(input("Nhập một số nguyên: ").strip())
        if is_perfect_square(n):
            print(f"{n} là số chính phương.")
        else:
            print(f"{n} không phải là số chính phương.")
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")
