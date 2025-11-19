# BT4.py - In các số nguyên tố < n
def primes_less_than(n):
    if n <= 2:
        return []
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    p = 2
    while p * p < n:
        if sieve[p]:
            for multiple in range(p*p, n, p):
                sieve[multiple] = False
        p += 1
    return [i for i, isprime in enumerate(sieve) if isprime]

if __name__ == "__main__":
    n = int(input("Nhập n: ").strip())
    print("Các số nguyên tố nhỏ hơn", n, "là:")
    print(primes_less_than(n))
