#Q)4)Computers are commonly used in encryption.
# A very simple form of encryption (more accurately "obfuscation") would be to remove the spaces from a message and reverse the resulting string.
# Write, and test, a function that takes a string containing a message and "encrypts" it in this way.

def encrypt_message_from_user():
    try:
        message = input("Enter a message: ")
        if not message:
            return "Empty message."

        encrypted_message = message.replace(" ", "")[::-1]
        return encrypted_message
    except Exception as e:
        print(f"Error: {e}")

encrypted_message = encrypt_message_from_user()
print(f"Encrypted Message: {encrypted_message}")

