# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

# Sample Output : {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}ascii_dict = {}
size = int(input("Enter the size of dictionary: "))
ascii_dict = {}
if size == 26:
    alphabet = [chr(ord('a')+ i) for i in range(26)]
    ascii_values = [ord(char) for char in alphabet]
    for i in range(26):
        ascii_dict[alphabet[i]] = ascii_values[i]
        print("dictionary:", ascii_values[i])
    else:
        print("Invalid size please enter 26 for a-z.")
