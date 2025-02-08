import random
import string


def generate_password():
    password = ''
    letters = string.ascii_letters
    numbers = string.digits
    symbols = ['#','%','&','@','$']

    for i in range(10):

     if i <7:   password += random.choice(letters)
     if i > 6 and i < 9:  password += random.choice(numbers)
     if i > 8:  password += random.choice(symbols)
    return password

print(generate_password())