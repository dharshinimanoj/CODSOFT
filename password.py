import random
import string

def generate_password(length):
    if length < 4:
        return "Password should be at least 4 characters long."

    # Characters to choose from
    letters = string.ascii_letters  # a-z + A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # !@#$%^&*() etc.

    all_chars = letters + digits + symbols

    # Ensure password includes at least one letter, digit, and symbol
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    password += random.choices(all_chars, k=length - 3)

    # Shuffle to prevent predictable order
    random.shuffle(password)

    return ''.join(password)

# --------- Main Program ----------
print("🔐 Password Generator")
try:
    user_input = int(input("Enter desired password length: "))
    result = generate_password(user_input)
    print("Generated Password: ", result)
except ValueError:
    print("Please enter a valid number.")
