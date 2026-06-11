# Week 1: Classical Cryptography Ciphers

This directory contains implementations of classical substitution ciphers used in cryptography.

## Overview

Classical ciphers are foundational cryptographic techniques that form the basis for understanding modern encryption methods. This week, we explore two fundamental substitution ciphers:

### 1. Caesar Cipher

The Caesar cipher is one of the simplest and most widely known encryption techniques.

**How it works:**
- Each letter in the plaintext is shifted a fixed number of positions down the alphabet
- Non-alphabetic characters are left unchanged
- The shift value typically ranges from 1 to 25

**Example:**
```
Plaintext:  HELLO
Shift: 3
Ciphertext: KHOOR
```

**Security:** The Caesar cipher is **NOT secure** and can be easily broken through:
- Brute force (only 26 possible shifts)
- Frequency analysis
- Pattern recognition

**File:** `caesar_cipher.py`

### 2. Vigenere Cipher

The Vigenere cipher is a polyalphabetic substitution cipher that improves upon the Caesar cipher by using a keyword.

**How it works:**
- A keyword is repeated to match the length of the plaintext
- Each letter is shifted by an amount determined by the corresponding key letter
- This creates multiple Caesar ciphers running in parallel

**Example:**
```
Plaintext:  ATTACKATDAWN
Key:        SECRETSECRET
Ciphertext: SXGPRQXVNBHQ
```

**Security:** While stronger than Caesar cipher, Vigenere is still vulnerable to:
- Kasiski examination (finding key length)
- Index of coincidence
- Known plaintext attacks
- Frequency analysis (with statistical methods)

**File:** `vigenere_cipher.py`

## Files

- **caesar_cipher.py** - Caesar cipher implementation with encryption, decryption, and brute-force attack
- **vigenere_cipher.py** - Vigenere cipher implementation with encryption and decryption
- **README.md** - This file
- **report.md** - Detailed analysis and security assessment

## Usage

### Caesar Cipher

```python
from caesar_cipher import caesar_encrypt, caesar_decrypt, caesar_bruteforce

# Encryption
encrypted = caesar_encrypt("Hello, World!", 3)
print(encrypted)  # Output: Khoor, Zruog!

# Decryption
decrypted = caesar_decrypt(encrypted, 3)
print(decrypted)  # Output: Hello, World!

# Brute force attack
for shift, text in caesar_bruteforce(encrypted):
    print(f"Shift {shift}: {text}")
```

### Vigenere Cipher

```python
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt

# Encryption
key = "SECRET"
encrypted = vigenere_encrypt("Hello, World!", key)
print(encrypted)  # Output: Zygzs, Ufmjb!

# Decryption
decrypted = vigenere_decrypt(encrypted, key)
print(decrypted)  # Output: Hello, World!
```

## Key Concepts

- **Substitution Cipher:** A cipher where each plaintext character is replaced with another character
- **Monoalphabetic:** Uses a single substitution alphabet (Caesar)
- **Polyalphabetic:** Uses multiple substitution alphabets (Vigenere)
- **Key/Keyword:** Secret information needed to encrypt/decrypt
- **Shift:** The number of positions to shift in the alphabet

## Learning Objectives

After studying these implementations, you should understand:

1. How substitution ciphers work at a fundamental level
2. The difference between monoalphabetic and polyalphabetic ciphers
3. Why these classical ciphers are not suitable for modern security needs
4. Basic cryptanalysis techniques
5. The foundation for more secure modern encryption methods

## Security Warning ⚠️

**These ciphers are for educational purposes only!** They should never be used for actual security needs:

- Both ciphers are completely broken cryptographically
- They can be cracked in seconds with modern computers
- Use modern encryption algorithms (AES, RSA, etc.) for real security
- Always use established cryptographic libraries rather than implementing your own

## Next Steps

- Implement frequency analysis to break Caesar cipher automatically
- Analyze the Vigenere cipher's vulnerabilities
- Explore advanced classical ciphers (Playfair, Enigma)
- Study modern symmetric encryption (AES)
- Learn about asymmetric encryption (RSA, ECC)

## References

- Wikipedia: Caesar Cipher - https://en.wikipedia.org/wiki/Caesar_cipher
- Wikipedia: Vigenere Cipher - https://en.wikipedia.org/wiki/Vigenere_cipher
- "The Code Breaker" by Walter Isaacson
- Cryptography course materials
