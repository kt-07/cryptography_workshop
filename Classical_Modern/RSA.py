# Python for RSA asymmetric cryptographic algorithm.
# For demonstration, values are
# relatively small compared to practical application
import math

public_key = None
private_key = None
n = 0

# To find GCD of 2 numbers
def gcd(a, h):
	temp = 0
	while(1):
		temp = a % h
		if (temp == 0):
			return h
		a = h
		h = temp

# For encryption
def encrypt(message):
    global n
    e = public_key
    encrpyted_text = 1
    while e:
        encrpyted_text *= message
        encrpyted_text %= n
        e -= 1
    
    return encrpyted_text


#  For Decryption
def decrypt( encrpyted_text):

    d = private_key
    decrypted = 1
    while d:
        decrypted *= encrpyted_text
        decrypted %= n
        d -= 1
    
    return decrypted


# first converting each character to its ASCII value and
# then encoding it then decoding the number to get the
# ASCII and converting it to character
def encoder(message):
    cipher_list = []
    # calling the encrypting function in encoding function
    for letter in message:
        cipher_list.append(encrypt(ord(letter)))
    return cipher_list

def decoder(encoded):
    s = ""
    # calling the decrypting function decoding function
    for num in encoded:
        s += chr(decrypt(num))
    return s


if __name__ == "__main__":
    p, q = 17, 19
    # p = int(input("Enter a prime number:"))
    # q = int(input("Enter another prime number:"))
    n = p*q
    phi = (p-1)*(q-1)
    e = 2
    while (e < phi):

        # e must be co-prime to phi and
        # smaller than phi.
        if(gcd(e, phi) == 1):
            break
        else:
            e = e+1

    # Private key (d stands for decrypt)
    # choosing d such that it satisfies
    # d*e = 1 + k * totient

    public_key = e
    d = 2

    while True:
        if ((d * e) % phi == 1):
            break
        d += 1
    private_key = d

    # Message to be encrypted
    message = input("Enter message to be encrypted: ")
    cipher = encoder(message)
    print("The encoded message(encrypted by public key): ", ''.join([str(x) for x in cipher]))
    decoded_msg = decoder(cipher)
    print("The decoded message(decrypted by private key): ", decoded_msg)
    