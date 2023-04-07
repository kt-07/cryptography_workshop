def KSAPRGA(key, message):
    # Key Scheduling Algorithm
    S = [0]*256
    for i in range(256):
      S[i]=i

    j = 0
    result=[]

    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudorandom Generator Algorithm
    i = j = 0
    for p in message:
        i = (i + 1) % 256
        j = (j + (S[i])) % 256
        S[i], S[j] = S[j], S[i]
        result.append(ord(p) ^ S[(S[i] + S[j]) % 256]) # Encryption/Decryption

    return result


if __name__ == "__main__":
    
    message=input("Enter the message to encrypt: ")
    key=input("Enter the key value: ")

    # Encryption
    cipher=KSAPRGA(key,message)
    
    # Converting Integer Output to String
    cipher_str=''
    for p in cipher: 
        cipher_str += chr(p)
    print("Encrypted message: ", cipher_str)

    # Decryption
    plaintext=KSAPRGA(key,cipher_str) 

    # Converting Integer Output to String
    plaintext_str=""
    for h in plaintext:
        plaintext_str+=chr(h)
    print("Decrypted message: ",plaintext_str)