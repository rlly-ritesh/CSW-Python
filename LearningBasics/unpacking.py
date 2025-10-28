import math
def prime_generator(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Example usage:
for prime in prime_generator(50):
    print(prime, end=" ")