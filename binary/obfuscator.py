import random

def obfuscate(binary_str):
    # define the patterns for obfuscation and deobfuscation
    obfuscate_patterns = ["01010101", "10101010"]
    deobfuscate_patterns = {"01010101": "000", "10101010": "1111"}

    # split the binary string into chunks of equal length
    chunk_size = 4
    binary_chunks = [binary_str[i:i+chunk_size] for i in range(0, len(binary_str), chunk_size)]

    # obfuscate any sequences of 000 or 1111
    obfuscated_chunks = []
    for chunk in binary_chunks:
        if chunk == "000" or chunk == "1111":
            obfuscated_chunks.append(random.choice(obfuscate_patterns))
        else:
            obfuscated_chunks.append(chunk)

    # join the obfuscated chunks back into a single string
    obfuscated_str = "".join(obfuscated_chunks)

    # return the obfuscated string
    return obfuscated_str

def deobfuscate(binary_str):
    # define the patterns for obfuscation and deobfuscation
    obfuscate_patterns = ["01010101", "10101010"]
    deobfuscate_patterns = {"01010101": "000", "10101010": "1111"}

    # split the binary string into chunks of equal length
    chunk_size = 4
    binary_chunks = [binary_str[i:i+chunk_size] for i in range(0, len(binary_str), chunk_size)]

    # deobfuscate any obfuscated chunks
    deobfuscated_chunks = []
    for chunk in binary_chunks:
        if chunk in deobfuscate_patterns:
            deobfuscated_chunks.append(deobfuscate_patterns[chunk])
        else:
            deobfuscated_chunks.append(chunk)

    # join the deobfuscated chunks back into a single string
    deobfuscated_str = "".join(deobfuscated_chunks)

    # return the deobfuscated string
    return deobfuscated_str

# prompt the user to choose an option from the menu
while True:
    print("1. Obfuscate binary string")
    print("2. Deobfuscate binary string")
    choice = input("Choose an option (1 or 2): ")
    if choice == "1":
        # prompt the user to enter a binary string
        binary_str = input("Enter a binary string: ")
        # obfuscate the binary string
        obfuscated_str = obfuscate(binary_str)
        # print the obfuscated string
        print("Obfuscated binary string:", obfuscated_str)
        break
    elif choice == "2":
        # prompt the user to enter an obfuscated binary string
        obfuscated_str = input("Enter an obfuscated binary string: ")
        # deobfuscate the binary string
        deobfuscated_str = deobfuscate(obfuscated_str)
        # print the deobfuscated string
        print("Deobfuscated binary string:", deobfuscated_str)
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")

