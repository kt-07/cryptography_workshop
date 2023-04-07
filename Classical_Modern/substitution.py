def sub_encrypt(message, key):
    cipher = ""
    for ch in message:
        if ch.isupper():
            cipher += key[ch] #For Upper case characters
        else:
            cipher += key[ch.upper()].lower() #For Lower case characters
    return cipher

def sub_decrypt(cipher, key):
    message = ""
    for ch in cipher:
        if ch.isupper():
            message += key[ch] #For Upper case characters
        else:
            message += key[ch.upper()].lower() #For Lower case characters
    return message

if __name__ == "__main__":
    #   User Input for message
    key = {'A':'R','B':'N','C':'X','D':'S','E':'W','F':'T','G':'V','H':'O','I':'Y','J':'Q','K':'U','L':'Z','M':'P','N':'B','O':'I','P':'H','Q':'J','R':'A','S':'D','T':'K','U':'F','V':'M','W':'L','X':'C','Y':'E','Z':'G'}
    message = input("Enter the message to encrypt: ")
    cipher = sub_encrypt(message, key)
    print("Encrypted message: ", cipher)

    key_inv = {x: v for v, x in key.items()}
    plaintext = sub_decrypt(cipher, key_inv)
    print("Decrypted message: ", plaintext)
  