import random

def odd_or_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

random_number = random.randint(1, 10)
print(odd_or_even(random_number))