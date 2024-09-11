
import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    number_criteria = re.search(r"[0-9]", password) is not None
    special_char_criteria = re.search(r"[\W_]", password) is not None

    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, {
        "Length (>= 8)": length_criteria,
        "Uppercase Letter": uppercase_criteria,
        "Lowercase Letter": lowercase_criteria,
        "Number": number_criteria,
        "Special Character": special_char_criteria,
    }

def main():
    password = input("Enter a password to assess its strength: ")
    strength, criteria = check_password_strength(password)
    print(f"Password Strength: {strength}")
    print("Criteria Met:")
    for criterion, met in criteria.items():
        status = "✓" if met else "✗"
        print(f"  {criterion}: {status}")

    if strength in ["Very Weak", "Weak", "Medium"]:
        print("\nSuggestions to improve your password:")
        if not criteria["Length (>= 8)"]:
            print("- Make the password at least 8 characters long.")
        if not criteria["Uppercase Letter"]:
            print("- Include at least one uppercase letter (A-Z).")
        if not criteria["Lowercase Letter"]:
            print("- Include at least one lowercase letter (a-z).")
        if not criteria["Number"]:
            print("- Include at least one number (0-9).")
        if not criteria["Special Character"]:
            print("- Include at least one special character (e.g., !, @, #, $, etc.).")

if __name__ == "__main__":
    main()