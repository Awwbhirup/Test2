def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def sum_of_primes(n):
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            return True
    return False
lst = list(map(int, input("Enter a list of integers separated by commas: ").split(",")))
result = [x for x in lst if sum_of_primes(x)]

print(result)