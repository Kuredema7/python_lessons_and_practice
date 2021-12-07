def prime_checker(number):
    is_prime_number = True
    for p in range(2, number - 1):
        if number % p == 0:
            is_prime_number = False

    if is_prime_number:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

prime_checker(number=4)