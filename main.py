from random import choice
from pyperclip import copy

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special = '!@#$%^&*_-'

def GeneratePassword(length: int = 12, alphanumeric: bool = True, specialChars: bool = True, copyToClipboard: bool = True) -> str:
    password = ''

    if length > 32: length = 32
    if length < 6: length = 6

    for i in range(length):
        if not alphanumeric and not specialChars:
            password += choice(alphabet)
        elif not alphanumeric and specialChars:
            password += choice(alphabet + special)
        elif alphanumeric and not specialChars:
            password += choice(alphabet + numbers)
        elif alphanumeric and specialChars:
            password += choice(alphabet + numbers + special)

    print('Sucessfully generated password!')

    if copyToClipboard:
        copy(password)
        print('Copied password to clipboard!')

    return password