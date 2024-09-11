def caesar_cipher(text, shift, mode='encrypt'):
    shift = shift % 26
    if mode == 'decrypt':
        shift = -shift  
    result = []
    for char in text:
        if char.isupper():
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            new_char = chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            new_char = char  
        result.append(new_char)
    
    return ''.join(result)

def main():
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    
    if mode in ['encrypt', 'decrypt']:
        result = caesar_cipher(text, shift, mode)
        print(f"Result: {result}")
    else:
        print("Invalid mode selected. Please choose either 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()

