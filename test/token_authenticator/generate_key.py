import random


def generate_random_two_digit_number():
    while True:
        digit1 = random.randint(0, 9)
        digit2 = random.randint(0, 9)

        if digit1 != digit2:
            return digit1 * 10 + digit2



number = generate_random_two_digit_number()
print(number)
