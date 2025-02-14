#Lab 4

def fibonacci(n):
    current_pos = 0
    prev_1 = 0
    prev_2 = 0
    for i in range(1, n+1):
        if i == 1:
            current_pos = 0
        elif i == 2:
            current_pos = 1
            prev_1 = 0
        elif i == 3:
            prev_1 = current_pos
            prev_2 = 0
            current_pos = prev_1 + prev_2
        elif i >= 4:
            prev_2 = prev_1
            prev_1 = current_pos
            current_pos = prev_1 + prev_2
    return current_pos

def is_prime (n):
    if n >= 0:
        for i in range(2, n):
            if n % i == 0:
                return False
    elif n < 0:
        for i in range(2, n, -1):
            if n % i == 0:
                return False
    return True

def print_prime_factors (n):
    print(f"{n} =", end = " ")
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                while n % i == 0:
                    n = n // i
                    print(f"{i} * ", end = " ")









