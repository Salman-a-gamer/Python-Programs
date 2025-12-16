from operator import index

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasor(ogtext, shift, encryptordecrypt):
    text = ''
    for ch in ogtext:
        index = alphabet.index(ch)
        index = index % 25
        if encryptordecrypt == 'decrypt':
            shift *= -1
        text += alphabet[index + shift]

    return text

'''
Without the alphabet list but with symbols......

def decrypt(encrypted_text, shift):
    decrypted_text = ''
    for ch in encrypted_text:
        decrypted_text += chr(ord(ch) - shift)
    return decrypted_text
'''
str = ceasor('hello', 3, 'encrypt')
print(str)
