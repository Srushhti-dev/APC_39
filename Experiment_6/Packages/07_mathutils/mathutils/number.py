def prime(n):
    if n < 2: return False
    return all(n % i for i in range(2, int(n**0.5)+1))
def palindrome(n): return str(n) == str(n)[::-1]
def armstrong(n):
    s=str(n); return sum(int(x)**len(s) for x in s)==n
