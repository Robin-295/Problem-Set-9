from sys import argv
import string 
# Get key from command-line argument
Key = int(argv[1])

plaintext = raw_input("Plaintext: ")

def caesar(plaintext, Key):
    ciphertext = ""
    for ch in plaintext:
        # Don't change numbers and symbols
        if (ch not in upper and ch not in lower) or ch in digit:
            return o
        else:
            # If uppercase
            if o in upper and o + Key % 26 in upper:
                return o + Key % 26
            # If lowercase
            elif o in lower and o + Key % 26 in lower:
                return o + key % 26

# append to string
x = (''.join(map(chr, caesar(plaintext, Key))))
# print string
print("ciphertext: ", x)