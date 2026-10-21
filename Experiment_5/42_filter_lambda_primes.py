def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, input("Enter numbers: ").split()))
primes = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers =", primes)
