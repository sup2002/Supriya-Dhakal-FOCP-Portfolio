#Q)5)Another way to hide a message is to include the letters that make it up within seemingly random text. The letters of the message might be every fifth character,
#for example. Write and test a function that does such encryption. It should randomly generate an interval (between 2 and 20), space the message out accordingly, and should fill the gaps with random letters. The function should return the encrypted message and the interval used.
#For example, if the message is "send cheese", the random interval is 2, and for clarity the random letters are not random:
#send cheese
#s e n d c h e e s e
#sxyexynxydxy cxyhxyexyexysxye

import random
import string

def encrypt_message_interval(message):
    if not message:
        return "Empty message.", None

    interval = random.randint(2, 20)
    encrypted_message = ""

    for i, char in enumerate(message):
        if char.isalpha():
            encrypted_message += char
        elif char.isspace():
            encrypted_message += " "
        else:
            encrypted_message += random.choice(string.ascii_letters)

        if (i + 1) % interval == 0:
            encrypted_message += " "

    return encrypted_message, interval

original_message = "send cheese"
encrypted_message, interval_used = encrypt_message_interval(original_message)
print(f"Original Message: {original_message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Interval Used: {interval_used}")
