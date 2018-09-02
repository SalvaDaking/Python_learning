while True:

    upper = 0
    lower = 0

    phrase = input("Introduce a phrase (type 'q' to quit): \n")

    if phrase.lower() == "q":
        break

    for letter in phrase:
        if letter.isalpha():
            if letter == letter.upper():
                upper += 1
            else:
                lower += 1

    print(f"\"{phrase}\" has {upper} uppercase and {lower} lowercase letters.\n")

print("Thanks for using the letter counter.")
