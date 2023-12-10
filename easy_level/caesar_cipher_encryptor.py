def caesarCipherEncryptor(string, key):
    return ''.join([shiftLetterByKey(character, key) for character in string])

def shiftLetterByKey(character, key):
    return chr(((ord(character) - 97 + key) % 26) + 97)
