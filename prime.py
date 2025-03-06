def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num

# Example usage
current = int(input("Enter a prime number: "))
print("The next prime is:", next_prime(current))
