is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 21, 23, 29, 31]

prime_numbers = list(filter(is_prime, numbers))

print("Простые числа:", prime_numbers)
