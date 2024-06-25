import itertools
import string

characters = '0123'
combinations = [''.join(p) for p in itertools.product(characters, repeat=4)]

letters = string.ascii_lowercase[:16]
two_char_combinations = [''.join(p) for p in itertools.product(letters, repeat=2)]
if len(combinations) > len(two_char_combinations):
    raise ValueError("Not enough unique two-character strings to represent all combinations.")

shorten_map = {combinations[i]: two_char_combinations[i] for i in range(len(combinations))}
reverse_map = {v: k for k, v in shorten_map.items()}

def encode_string(s, mapping):
    chunks = [s[i:i+4] for i in range(0, len(s), 4)]
    shortened_chunks = [mapping[chunk] for chunk in chunks]
    return ''.join(shortened_chunks)

def decode_string(s, mapping):
    chunks = [s[i:i+2] for i in range(0, len(s), 2)]
    decoded_chunks = [mapping[chunk] for chunk in chunks]
    return ''.join(decoded_chunks)

while True:
    print("\n=== Main Menu ===")
    print("1. Encode a string")
    print("2. Decode a string")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':
        input_string = input("Enter the string to encode (only '0', '1', '2', '3' allowed): ").strip()
        encoded_string = encode_string(input_string, shorten_map)
        print(f"Encoded string: {encoded_string}")

    elif choice == '2':
        input_string = input("Enter the string to decode (two-character segments): ").strip()
        decoded_string = decode_string(input_string, reverse_map)
        print(f"Decoded string: {decoded_string}")

    elif choice == '3':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
