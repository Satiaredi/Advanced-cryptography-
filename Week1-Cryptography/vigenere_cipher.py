"""Vigenere Cipher Implementation

A polyalphabetic substitution cipher that uses a keyword to encrypt text.
"""

def vigenere_encrypt(plaintext, key):
    """
    Encrypt text using Vigenere cipher.
    
    Args:
        plaintext (str): The text to encrypt
        key (str): The encryption key (must contain only letters)
    
    Returns:
        str: Encrypted text
    """
    if not key or not key.isalpha():
        raise ValueError("Key must contain only alphabetic characters")
    
    result = ""
    key_index = 0
    key_upper = key.upper()
    
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            
            # Get the shift from the current key character
            shift = ord(key_upper[key_index % len(key)]) - ord('A')
            
            # Shift the character
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += shifted if is_upper else shifted.lower()
            
            # Move to next key character
            key_index += 1
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result


def vigenere_decrypt(ciphertext, key):
    """
    Decrypt text using Vigenere cipher.
    
    Args:
        ciphertext (str): The text to decrypt
        key (str): The encryption key
    
    Returns:
        str: Decrypted text
    """
    if not key or not key.isalpha():
        raise ValueError("Key must contain only alphabetic characters")
    
    result = ""
    key_index = 0
    key_upper = key.upper()
    
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            
            # Get the shift from the current key character (negate for decryption)
            shift = ord(key_upper[key_index % len(key)]) - ord('A')
            
            # Reverse the shift
            shifted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result += shifted if is_upper else shifted.lower()
            
            # Move to next key character
            key_index += 1
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result


if __name__ == "__main__":
    # Example usage
    message = "Hello, World!"
    key = "SECRET"
    
    encrypted = vigenere_encrypt(message, key)
    decrypted = vigenere_decrypt(encrypted, key)
    
    print(f"Original: {message}")
    print(f"Key: {key}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    
    # Test with different messages
    print("\n--- Additional Tests ---")
    messages = ["ATTACKATDAWN", "The quick brown fox", "123 ABC"]
    
    for msg in messages:
        enc = vigenere_encrypt(msg, key)
        dec = vigenere_decrypt(enc, key)
        print(f"Message: {msg}")
        print(f"Encrypted: {enc}")
        print(f"Decrypted: {dec}")
        print()
