#Task 4
def filter_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

numbers = list(map(int, input("Enter numbers : ").split()))

prime_numbers = list(filter(lambda x: filter_prime(x), numbers))

print("Prime numbers:", prime_numbers)

