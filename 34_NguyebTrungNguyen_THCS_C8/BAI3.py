# BT3.py - Rút gọn phân số
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def reduce_fraction(num, den):
    if den == 0:
        raise ZeroDivisionError("Mẫu phải khác 0.")
    g = gcd(num, den)
    num //= g
    den //= g
    # để dấu ở tử số
    if den < 0:
        num = -num
        den = -den
    return num, den

if __name__ == "__main__":
    num = int(input("Nhập tử số: ").strip())
    den = int(input("Nhập mẫu số: ").strip())
    try:
        a, b = reduce_fraction(num, den)
        print(f"Phân số tối giản: {a}/{b}")
    except ZeroDivisionError as e:
        print(e)
