import sys

# Python script to convert string to binary

# prompt the user to enter a string
print("Enter a string (press Ctrl-D when finished):")

# read input from stdin
input_str = ''.join(line for line in sys.stdin)

# convert each character of the input string to its binary representation
binary_str = ''.join(format(ord(c), '08b') for c in input_str)

# print the binary representation of the input string
print(binary_str)
