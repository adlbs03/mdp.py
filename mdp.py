import string

alpha_lower = list(string.ascii_lowercase)
alpha_upper = list(string.ascii_uppercase)

special_chars = set('[@_!#$%^&*()<>?/\\|}{~:]')

password = input("Enter a password : ")

while len(password) < 6:
    password = input("Enter a password with more than 6 chars : ")

while not any(c.isupper() for c in password):
     password = input("Enter a password with a minimum of one maj : ")

decale_lower = alpha_lower[3:] + alpha_lower[:3]
decale_upper = alpha_upper[3:] + alpha_upper[:3]

like_lower = dict(zip(alpha_lower, decale_lower))
like_upper = dict(zip(alpha_upper, decale_upper))

result_alpha = ""
result_digit = ""
result_spe = ""

for c in password:
    if c.isalpha() and c.islower():
        result_alpha += like_lower[c]
    elif c.isalpha() and c.isupper():
        result_alpha += like_upper[c]
    elif c.isdigit():
        result_digit += c * 2
    elif c in special_chars:
        result_spe += c
    else:
        result_alpha += c

print(result_alpha + result_digit + result_spe)

