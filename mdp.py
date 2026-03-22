import string

alpha_lower = list(string.ascii_lowercase)
alpha_upper = list(string.ascii_uppercase)

password = input("Enter a password : ")

while len(password) < 6:
    password = input("Enter a password : ")

decale_lower = alpha_lower[3:] + alpha_lower[:3]
decale_upper = alpha_upper[3:] + alpha_upper[:3]

like_lower = dict(zip(alpha_lower, decale_lower))
like_upper = dict(zip(alpha_upper, decale_upper))

result = ""

for c in password:
    if c.isalpha() and c.islower():
        result += like_lower[c]
    elif c.isalpha() and c.isupper():
        result += like_upper[c]
    else:
        result += c

print(result)