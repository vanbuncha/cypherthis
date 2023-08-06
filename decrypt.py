from cryptography.fernet import Fernet

def decrypt_chunk(chunk, key):
    fernet = Fernet(key)
    decrypted_chunk = fernet.decrypt(chunk)
    return decrypted_chunk.decode()

if __name__ == "__main__":
    encrypted_file = input("Enter the name of the encrypted file: ")
    key_file = input("Enter the name of the file containing the encryption key: ")

    # Read the encryption key from the key file
    with open(key_file, "rb") as key_file:
        key = key_file.read()

    # Decrypt the encrypted file in chunks and print the decrypted output
    with open(encrypted_file, "rb") as file:
        while True:
            chunk = file.read(4096)  # Modify this value to adjust the chunk size
            if not chunk:
                break
            decrypted_chunk = decrypt_chunk(chunk, key)
            print(decrypted_chunk, end='')

