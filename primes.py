"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

# NOTE: Don't need to check past sqrt(x)
def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if not(x % i):
            return False

    return True

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Invalid number of primes, number_of_primes should be more than 0")

    list = []
    nprimes_acc = 0 # Number of primes accumulated thus far
    cur_int = 2 # Current integer to test

    while nprimes_acc < number_of_primes:
        if is_prime(cur_int):
            list.append(cur_int)
            nprimes_acc += 1

        cur_int += 1

    return list
