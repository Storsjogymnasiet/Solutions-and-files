print("Skriv en mening som innehåller åäö")
sentence = input()

new_sentence = ""

for letter in sentence:

    is_uppercase = False

    if letter.upper() == letter:
        is_uppercase = True
    else:
        is_uppercase = False

    if letter.lower() == "ö":
        if is_uppercase:
            new_sentence += "O"
        else:
            new_sentence += "o"
    elif letter.lower() == "ä" or letter.lower() == "å":
        if is_uppercase:
            new_sentence += "A"
        else:
            new_sentence += "a"
    else:
        new_sentence += letter

print(new_sentence)