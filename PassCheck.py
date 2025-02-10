import re

def check_password_strength(password: str) -> bool:
    # Minimum length of 8 characters
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    
    # Contains both uppercase and lowercase letters
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        print("Password must contain both uppercase and lowercase letters.")
        return False
    
    # Contains at least one digit (0-9)
    if not re.search(r'\d', password):
        print("Password must contain at least one digit.")
        return False
    
    # Contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("Password must contain at least one special character.")
        return False
    
    return True

if __name__ == "__main__":
    password = input("Enter a password: ")
    
    if check_password_strength(password):
        print("Strong password!")
    else:
        print("Weak password. Please try again.")
