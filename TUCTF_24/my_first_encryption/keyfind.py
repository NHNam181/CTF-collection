def find_xor_key(encrypted_file, known_plaintext, start_index=0):
    with open(encrypted_file, 'rb') as f:
        data = f.read()
    
    # Slice the encrypted data where the known plaintext aligns
    encrypted_slice = data[start_index:start_index + len(known_plaintext)]
    
    # XOR each byte of the encrypted slice with the known plaintext
    key = [enc ^ plain for enc, plain in zip(encrypted_slice, known_plaintext)]
    return key

# Parameters
encrypted_file = 'flag.jpeg'  # Replace with your encrypted file
known_plaintext = b'\xFF\xD8\xFF'  # Known JPEG header
start_index = 0  # Typically, the header starts at the beginning

key = find_xor_key(encrypted_file, known_plaintext, start_index)
print(f"XOR Key: {key}")
