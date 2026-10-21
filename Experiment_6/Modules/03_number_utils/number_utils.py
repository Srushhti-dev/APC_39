def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

def is_palindrome(n): return str(n) == str(n)[::-1]

def is_armstrong(n):
    digits = str(n)
    return sum(int(d) ** len(digits) for d in digits) == n

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n
