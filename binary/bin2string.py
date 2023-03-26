import sys

# Python script to decrypt binary string

# prompt the user to enter a binary string
print("Enter a binary string (press Ctrl-D when finished):")

# read input from stdin
binary_str = ''.join(line for line in sys.stdin)

# split the binary string into 8-bit chunks
binary_chunks = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]

# convert each 8-bit chunk to its corresponding character
result = ''
for binary in binary_chunks:
    char = chr(int(binary, 2))
    result += char

# print the decrypted string
print(result)

