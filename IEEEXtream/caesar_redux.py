def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext


def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


# Function to process n messages
def process_messages(n):
    messages = []
    for _ in range(n):
        shift = int(input())
        message = input().strip()
        messages.append((shift, message))
    return messages


n = int(input())  # Read the number of messages

messages = process_messages(n)  # Read and process n lines of input

for shift, text in messages:
    if " the " in text.lower():
        is_plaintext = True
    else:
        is_plaintext = False

    if is_plaintext:
        decrypted_text = caesar_cipher_decrypt(text, shift)
        print(decrypted_text)
    else:
        encrypted_text = caesar_cipher_encrypt(text, shift)
        print( encrypted_text)