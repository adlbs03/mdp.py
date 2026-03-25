import string
import random

alpha_lower = list(string.ascii_lowercase)
alpha_upper = list(string.ascii_uppercase)

special_chars = set('[@_!#$%^&*()<>?/\\|}{~:]')

password = input("Enter a password : ")

while len(password) < 6:
    password = input("Enter a password with more than 6 chars : ")

while not any(c.isupper() for c in password):
     password = input("Enter a password with a minimum of one maj : ")

result_alpha = ""
result_digit = ""
result_spe = ""

for c in password:
    decale_lower = random.choice(alpha_lower)
    decale_upper = random.choice(alpha_upper)
    if c.isalpha() and c.islower():
        result_alpha += decale_lower
    elif c.isalpha() and c.isupper():
        result_alpha += decale_upper
    elif c.isdigit():
        result_digit += c * 2
    elif c in special_chars:
        result_spe += c
    else:
        result_alpha += c

print(result_alpha + result_digit + result_spe)

