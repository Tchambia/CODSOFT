# Password Generator Application
import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for better security!")
        return None

    # Character pools for password generation
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure the password has at least one of each character type
    password = [
        random.choice(lower_case),
        random.choice(upper_case),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password with random choices from all pools
    all_chars = lower_case + upper_case + digits + special_chars
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password to make it random
    random.shuffle(password)

    return ''.join(password)

# Main program
def main():
    print("--- Password Generator ---")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive integer!")
        else:
            password = generate_password(length)
            if password:
                print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()
