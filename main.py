from generator import generate_password

def get_user_input():
    print("🔐 Password Generator")
    length = int(input("Enter password length (e.g. 12): "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    return length, use_upper, use_lower, use_digits, use_symbols

if __name__ == "__main__":
    try:
        length, upper, lower, digits, symbols = get_user_input()
        password = generate_password(length, upper, lower, digits, symbols)
        print(f"\nYour generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
