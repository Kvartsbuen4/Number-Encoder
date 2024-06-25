import itertools
import string
import random
#your list of numbers must be a multiple of 4
# Define the characters and generate combinations of length 4
characters = '0123456789'
combinations = [''.join(p) for p in itertools.product(characters, repeat=4)]

# Generate random 3-letter combinations
letters = string.ascii_lowercase
three_char_combinations = [''.join(p) for p in itertools.product(letters, repeat=3)]

# Ensure there are enough unique three-character strings to represent all combinations
if len(combinations) > len(three_char_combinations):
    raise ValueError("Not enough unique three-character strings to represent all combinations.")

# Shuffle the three_char_combinations to ensure randomness
random.shuffle(three_char_combinations)

# Create the mapping dictionaries
shorten_map = {combinations[i]: three_char_combinations[i] for i in range(len(combinations))}
reverse_map = {v: k for k, v in shorten_map.items()}


def encode_string(s, mapping):
    chunks = [s[i:i + 4] for i in range(0, len(s), 4)]
    shortened_chunks = [mapping[chunk] for chunk in chunks]
    return ''.join(shortened_chunks)


def decode_string(s, mapping):
    chunks = [s[i:i + 3] for i in range(0, len(s), 3)]
    decoded_chunks = [mapping[chunk] for chunk in chunks]
    return ''.join(decoded_chunks)


while True:
    print("\n=== Main Menu ===")
    print("1. Encode a string")
    print("2. Decode a string")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':
        input_string = input("Enter the string to encode (only digits '0'-'9' allowed): ").strip()

        # Check if input is valid
        if any(c not in characters for c in input_string):
            print("Invalid input string. Only digits '0'-'9' are allowed.")
            continue

        # Ensure the input length is a multiple of 4
        if len(input_string) % 4 != 0:
            print("Input string length must be a multiple of 4.")
            continue

        encoded_string = encode_string(input_string, shorten_map)
        print(f"Encoded string: {encoded_string}")

    elif choice == '2':
        input_string = input("Enter the string to decode (three-character segments): ").strip()

        # Check if input is valid
        if len(input_string) % 3 != 0:
            print("Input string length must be a multiple of 3.")
            continue

        decoded_string = decode_string(input_string, reverse_map)
        print(f"Decoded string: {decoded_string}")

    elif choice == '3':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
