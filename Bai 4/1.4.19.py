def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

P = tuple(i for i in range(2, 1_000_000) if is_prime(i))
print("Tuple P gồm các số nguyên tố nhỏ hơn 1 triệu:")
print(P)
