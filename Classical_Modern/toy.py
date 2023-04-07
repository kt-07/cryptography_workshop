#   function to convert string to Binary
def str_to_binary(string):
    # Initialize empty list to store binary values
    binary_list = []
    # Iterate through each character in the string
    for char in string:
        # Convert character to binary, pad with leading zeroes and append to list
        binary_list.append(bin(ord(char))[2:].zfill(8))
    # Join the binary values in the list and return as a single string
    return ''.join(binary_list)

#   Substitution round (Inverse = True, for inverse substitution)
def substitution(data, Inverse=False):
    inversesbox = [0] * 16
    for i, val in enumerate(substitutionbox): inversesbox[val] = i
    hexaconvert = format(data, '016b')
    sustitutionblock = [hexaconvert[i:i+4] for i in range(0, 16, 4)]
    if not Inverse: sustitutionblock = [substitutionbox[int(j, 2)] for j in sustitutionblock]
    else: sustitutionblock = [inversesbox[int(j, 2)] for j in sustitutionblock]
    result = int(''.join(format(j, '04b') for j in sustitutionblock), 2)
    return result


#   Permutation round (Inverse = True, for inverse permutation)
def permutation(data,Inverse=False):
    binarystring = format(data, '016b')
    binary = ''
    if not Inverse: 
        for i in range(16): binary += binarystring[permutationtable[i]]
    else: 
        for i in range(16): binary = binarystring[15 - permutationtable[i]] + binary
    binary = int(binary, 2)
    return binary

#   key mixing process
def key_mxn(data, key): return data ^ key

# key scheduling algorithm
def KSA(key):
    s_key=[int(key[i:i+16],2) for i in range(5)]
    return s_key

# Encryption function
def encryption(data):
    for i in range(4):
        data = substitution(data)
        data = permutation(data)
        data = key_mxn(data, subkeys[i])
    data = key_mxn(data, subkeys[-1])
    return data

#Decryption Function
def decryption(data):
    data = key_mxn(data, subkeys[-1])
    for i in range(3, -1, -1):
        data = key_mxn(data, subkeys[i])
        data = permutation(data,Inverse=True)
        data = substitution(data,Inverse=True)
    return data

substitutionbox = [0xe, 0x4, 0xd, 0x1, 0x2, 0xf, 0xb, 0x8, 0x3, 0xa, 0x6, 0xc, 0x5, 0x9, 0x0, 0x7]
permutationtable = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]
key_str = input('Enter Secret Key : ')
key = str_to_binary(key_str)

subkeys=KSA(key)



if __name__ == "__main__":
    #   Take user input in plain text format, then encode it to utf-8 and convert to binary.
    message=input('Enter message: ')
    message=message.encode('utf-8')
    binary_msg = ''.join(format(k, '08b') for k in bytearray(message)) 

    # Encryption Block by Block
    encypted_block_list=[]
    for block in range(0,len(binary_msg),16): 
        encypted_block_list.append(encryption(int(binary_msg[block:block+16],2)))
    cipher_bin = ''.join(format(block, '016b') for block in encypted_block_list)
    # print("Encrypted message in Binary: ", cipher_bin)

    # Converting Encrypted Message from Binary to String
    encrypted_msg_lst = [chr(int(cipher_bin[i:i+8], 2)) for i in range(0, len(cipher_bin), 8)]
    encrypted_msg=''.join(encrypted_msg_lst)
    print("Encrypted Message : ", encrypted_msg)

    # Decryption Block by Block
    cipher_bin = ''.join(format(ord(i), '08b') for i in encrypted_msg) # String to Binary for decryption
    decrypted_block_list=[]
    for block in range(0,len(cipher_bin),16): 
        decrypted_block_list.append(decryption(int(cipher_bin[block:block+16],2)))
    decrypted_msg_bin=''.join(format(block, '016b') for block in decrypted_block_list)

    # Converting Decrypted Message from Binary to String
    decrypted_msg_lst = [chr(int(decrypted_msg_bin[i:i+8], 2)) for i in range(0, len(decrypted_msg_bin), 8)]
    decrypted_msg=''.join(decrypted_msg_lst)
    print("Decrypted Message : ", decrypted_msg)
            