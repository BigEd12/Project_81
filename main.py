from dictionary import morse_dict
from art import logo


def encrypt(word):
    output = ""
    for letter in word:
        if letter == " ":
            output += " | "
        else:
            output += morse_dict[letter] + " "
    return output


def decrypt(word):
    split_word = word.split()
    output = ""
    for i in range(len(split_word)):
        if split_word[i] == "|":
            output += " "
        else:
            for key, value in morse_dict.items():
                if split_word[i] == value:
                    output += key
    return output

print(logo)
print("Welcome to the Morse Code converter.\n I can convert text to Morse Code, or vice versa.")
if input("Do you want to encrypt or decrypt? Type 'e' or 'd':\n") == "e":
    word = input("What would you like to encrypt?\n").lower()
    print(f"Your word {word} has been encrypted to: {encrypt(word)}")
else:
    word = input("What would you like to decrypt?\n")
    print(f"Your Morse code ({word}) has been decrypted as: {decrypt(word)} ")




