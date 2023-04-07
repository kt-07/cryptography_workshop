import random
# conversion of ASCII to Binary
def ascii_to_bin(ascii_str):
    byte_array = ascii_str.encode()
    binary_int = int.from_bytes(byte_array, "big")
    binary_string = bin(binary_int)
    return binary_string[2:]

# conversion of Binary to ASCII
def bin_to_ascii(binary_str):
    binary_str = '0b'+binary_str
    binary_int = int(binary_str, 2)
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    return ascii_text

# to generate random binary key
def random_key(N):
	S = ""
	for i in range(N):
		x = random.randint(0, 1)
		S += str(x)
	return S

def one_time_pad(data_bin, key_bin):
    n = len(data_bin)
    res = ""
    for i in range(n):
        if (data_bin[i] == key_bin[i]):
            res += "0"
        else:
            res += "1"
    return res

if __name__ == "__main__":
    data = input("Enter data : ")
    data_bin = ascii_to_bin(data)
    print("Data in Binary : ", data_bin)

    key_bin = random_key(len(data_bin))
    print("Key in Binary : ", key_bin)

    encrypted_bin = one_time_pad(data_bin, key_bin)
    print("\nEncrypted data in Binary : ", encrypted_bin)
    # cipher = bin_to_ascii(encrypted_bin)
    # print("Cipher : ", cipher)

    decrypted_bin = one_time_pad(encrypted_bin, key_bin)
    print("\nDecrypted data in Binary : ", decrypted_bin)
    plaintext = bin_to_ascii(decrypted_bin)
    print("Plaintext : ", plaintext)






