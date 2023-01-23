from dictionary import morse_dict

def convert():
    string = input("Welcome to the Text-to-Morse-Code. Please enter the message you'd like to convert to Morse Code:\n").lower()
    input_as_list = [*string]
    try:
        output = [morse_dict[letter] for letter in input_as_list]
    except KeyError:
        print("You've entered an unknown character.")

    else:
        str_join = " ".join(output)
        print("Your message in Morse:", str_join)

convert()