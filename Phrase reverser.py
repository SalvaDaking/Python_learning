while True:

    phrase = input("Introduce a phrase (type 'q' to quit): \n")

    if phrase.lower() == "q":
        break

    words = phrase.split()

    print(" ".join(words[::-1]))

print("Thanks for using the Phrase reverser.")
