# def greet():
#     print("WELCOME TO MY PROGRAM!!!")
#     print("I hope your are having a good day")
#
#
# greet()


# FUNCTIONS THAT ALLOW INPUT

# def greet_with_name(name):
#     print("WELCOME TO MY PROGRAM!!!")
#     print(f"Hello {name}")
#     print(f"How is your day going {name}? ")
#
#
# greet_with_name("Aaden")  # IT'S UNTIL YOU CALL THE FUNCTION THAT YOU CAN PASS THE NAME CHOSEN AS INPUT.

# FUNCTIONS THAT ALLOW MULTIPLE INPUT

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
#
#
# # greet_with(name="Aaden", location="Nashville")
#
# greet_with(location="Nashville", name="Aaden")
# def greet():

print("WELCOME TO MY PROGRAM!!!")
print("I hope your are having a good day, I will be helping you encrypt and decrypt any word of your choice.")


def play_game():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
    text = input("Type your message:").lower()
    shift = int(input("Type the shift number:"))

    def encrypt(plain_text, shift_num):
        cipher_text = ""
        alphabet_length = len(alphabet)
        for letter in plain_text:
            og_position = alphabet.index(letter)
            new_postition = (og_position + shift_num) % alphabet_length
            new_letter = alphabet[new_postition]
            cipher_text += new_letter
        print(f"The encoded text is: {cipher_text}")

    # encrypt(plain_text=text, shift_num=shift)

    def decrypt(cipher_text, shift_num):
        plain_text = ""
        alphabet_length = len(alphabet)
        for letter in cipher_text:
            og_position = alphabet.index(letter)
            new_postition = (og_position - shift_num) % alphabet_length
            new_letter = alphabet[new_postition]
            plain_text += new_letter
        print(f"The encoded text is: {plain_text}")

    # decrypt(cipher_text=text, shift_num=shift)

    if direction == "encode":
        encrypt(plain_text=text, shift_num=shift)
    else:
        decrypt(cipher_text=text, shift_num=shift)


while True:
    play_game()
    play_again = input("Do you want to cipher another word? (yes/no): ").lower()
    if play_again != "yes":
        print("THANKS FOR USING MY CIPHER. HAVE A GOOD DAY!!!")
        break
