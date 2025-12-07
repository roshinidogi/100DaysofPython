alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def caesar(encode_decode, original_text, shift_amount):
    modified_text = ""
    if encode_decode == "decode":
        shift_amount = shift_amount * -1
    for letter in original_text:
        if letter in alphabet:
            new_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            modified_text += alphabet[new_position]
        else:
            modified_text += letter
    print(f"Your {direction}d message is: {modified_text}")

caesar(direction, text, shift)
should_continue = True
while should_continue:
    input_text = input("Type 'yes' if you want to go again, otherwise type 'no': \n")
    if input_text == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
        text = input("Type your message: \n").lower()
        shift = int(input("Type the shift number: \n"))
        caesar(direction, text, shift)
    else:
        should_continue = False
        print("Goodbye!")

