from cryptography.fernet import Fernet
import sys

def divide_into_chunks(text, chunk_size=100):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def encrypt_text(text, key):
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode()).decode()
    return encrypted_text

if __name__ == "__main__":
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file for the encrypted text: ")
    key_name = input("Enter the name of the key file: ")

    with open(input_file, "r") as file:
        text_to_encrypt = file.read()

    key = Fernet.generate_key().decode()

    encrypted_text = encrypt_text(text_to_encrypt, key)

    # Formatting the encrypted text into chunks
    formatted_encrypted_text = "\n".join(divide_into_chunks(encrypted_text))

    with open(output_file, "w") as file:
        file.write(formatted_encrypted_text)

    with open(key_name, "w") as key_file:
        key_file.write(key)

    print("Text successfully encrypted and saved to", output_file)
    print("Encryption key saved to", key_name)
