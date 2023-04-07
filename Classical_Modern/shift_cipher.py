def encryption_shift(message, key):
    cipher = ""
    for ch in message:
        #  Check if message is is Alpha Numeric or not
        if (ch.isalnum()):
            # lower case characters
            if (ch.islower()):
                ch = chr((ord(ch) - ord('a') + key) % 26 + ord('a'))

            # uppercase characters
            if (ch.isupper()):
                ch = chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
                
            # numbers
            if (ch.isdigit()):
                ch = chr((ord(ch) - ord('0') + key) % 10 + ord('0'))

        #  Invalid Character in Message
        else:
            print("Invalid Message")
            break

        cipher += ch    
    return cipher

def decryption_shift(cipher, key):
    message = ""
    for ch in cipher:
        #  Check if message is is Alpha Numeric or not
        if (ch.isalnum()):
            # lower case characters
            if (ch.islower()):
                ch = chr((ord(ch) - ord('a') - key + 26) % 26 + ord('a'))

            # uppercase characters
            if (ch.isupper()):
                ch = chr((ord(ch) - ord('A') + 26 - key) % 26 + ord('A'))
                
            # numbers
            if (ch.isdigit()):
                ch = chr((ord(ch) - ord('0') + 26 - key) % 10 + ord('0'))

        #  Invalid Character in Message
        else:
            print("Invalid Message")
            break

        message += ch    
    return message

if __name__ == "__main__":
    # User Input for message
    message = input("Enter a message to encrypt: ")
    #    User Input for key
    key = int(input("Enter the key: "))
    cipher = encryption_shift(message, key)
    print("Encrypted message: ", cipher)

    
    plaintext = decryption_shift(cipher, key)
    print("Decrypted message: ", plaintext)



