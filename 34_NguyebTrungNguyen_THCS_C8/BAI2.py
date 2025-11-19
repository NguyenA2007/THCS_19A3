# BT2.py - Tìm UCLN của 2 số
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = int(input("Nhập a: ").strip())
    b = int(input("Nhập b: ").strip())
    print(f"Ước chung lớn nhất của {a} và {b} là {gcd(a,b)}")
