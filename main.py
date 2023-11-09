import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789'

number = input('Amount of passwords to generate: ')

try:
    number = int(number)
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

length = input('Your password length: ')

try:
    length = int(length)
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

print('\nhere are your passwords: ')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)