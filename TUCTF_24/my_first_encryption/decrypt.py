def xor_decrypt(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        data = f.read()
    # Apply XOR decryption
    decrypted_data = bytearray([b ^ key[i % len(key)] for i, b in enumerate(data)])
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

# Parameters
input_file = 'flag.jpeg'   # Replace with your encrypted file
output_file = 'decrypted.jpeg'  # Output file for the decrypted image
key = [48, 48, 48]  # XOR key

xor_decrypt(input_file, output_file, key)
print(f"Decryption completed! The decrypted file is saved as {output_file}.")
