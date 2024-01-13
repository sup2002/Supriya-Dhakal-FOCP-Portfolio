#Q)6)Write a program that decrypts messages encoded as above.

import string

def decrypt_message(encrypted_message, interval_used):
    decrypted_message = ''.join(
        char if char.isalpha() else ''
        for i, char in enumerate(encrypted_message) if (i + 1) % (interval_used + 1) == 0
    )

    return decrypted_message

encrypted_message = "sxyexynxydxy cxyhxyexyexysxye"
interval_used = 2
decrypted_message = decrypt_message(encrypted_message, interval_used)
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
