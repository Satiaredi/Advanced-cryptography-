"""Caesar Cipher Implementation

A classical substitution cipher that shifts each letter by a fixed number of positions.
"""

def caesar_encrypt(plaintext, shift):
    """
    Encrypt text using Caesar cipher.
    
    Args:
        plaintext (str): The text to encrypt
        shift (int): The shift value (1-25)
    
    Returns:
        str: Encrypted text
    """
    result = ""
    for char in plaintext:
        if char.isalpha():
            # Determine if uppercase or lowercase
            is_upper = char.isupper()
            char = char.upper()
            
            # Shift the character
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += shifted if is_upper else shifted.lower()
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result


def caesar_decrypt(ciphertext, shift):
    """
    Decrypt text using Caesar cipher.
    
    Args:
        ciphertext (str): The text to decrypt
        shift (int): The shift value used for encryption
    
    Returns:
        str: Decrypted text
    """
    # Decryption is just encryption with negative shift
    return caesar_encrypt(ciphertext, -shift)


def caesar_bruteforce(ciphertext):
    """
    Attempt to break Caesar cipher by trying all possible shifts.
    
    Args:
        ciphertext (str): The encrypted text
    
    Returns:
        list: List of tuples (shift, decrypted_text) for all 26 possible shifts
    """
    results = []
    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        results.append((shift, decrypted))
    
    return results


if __name__ == "__main__":
    # Example usage
    message = "Hello, World!"
    shift = 3
    
    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    
    print(f"Original: {message}")
    print(f"Encrypted (shift={shift}): {encrypted}")
    print(f"Decrypted: {decrypted}")
    print("\nBruteforce attempts:")
    for s, text in caesar_bruteforce(encrypted):
        print(f"Shift {s}: {text}")
