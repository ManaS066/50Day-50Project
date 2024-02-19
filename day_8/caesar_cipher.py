from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar_cipher(text, direction, shift_amt):
    end = ''
    if direction == "decode":
        shift_amt *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_pos = (position + shift_amt) % 26
            end += alphabet[new_pos]
        else:
            end += char
    print(f"The {direction} text is {end}")

while True:
    direction = input("Enter 'encode' for encoding and 'decode' for decoding: ").lower()
    text = input(f"Type your message you want to {direction}: ").lower()
    temp = int(input("Enter the shifting bits: "))
    shift = temp % 26
    caesar_cipher(text, direction, shift)
    repeat = input("If you want to continue, type 'yes'; otherwise, type 'no': ").lower()
    if repeat != 'yes':
        print("GOOD BYE !!")
        break


# def encrypt(plain_text,shift_amt):
#     cypher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
        
#         new_posi=int(position+shift_amt)
#         if (new_posi > 26):
#             new_posi-=26
#         new_letter=alphabet[new_posi]
#         cypher_text+=new_letter
#     print("the encodeed text is",cypher_text)


# def decrypt(plain_text,shift_amt):
#     cypher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
        
#         new_posi=int(position-shift_amt)
#         if (new_posi <=0):
#             new_posi+=26
#         new_letter=alphabet[new_posi]
#         cypher_text+=new_letter
#     print("the decded text is",cypher_text)
    