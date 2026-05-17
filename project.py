import string
import secrets as random
import csv

def main():
    password = input("Enter a password: ")

    validated = validate_password(password)
    transformed = transform_password(validated)

    with open("history.txt", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([validated, transformed])

    print(f"New password: {transformed}")


def validate_password(password):
    while len(password) < 6:
        password = input("Password must contain at least 6 characters: ")

    while not any(c.isupper() for c in password):
        password = input("Password must contain at least one uppercase letter: ")

    return password


def get_special_chars():
    return "@_!#$%^&*()<>?/\\|}{~:"


def transform_password(password):
    result = ""

    for c in password:

        if c.islower():
            result += random.choice(string.ascii_lowercase)

        elif c.isupper():
            result += random.choice(string.ascii_uppercase)

        elif c.isdigit():
            if int(c) < 3:
                result += c * 2
            else:
                result += c

        elif c in get_special_chars():
            result += c

        else:
            result += c

    return result


def password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in get_special_chars() for c in password):
        score += 1

    return score


if __name__ == "__main__":
    main()

