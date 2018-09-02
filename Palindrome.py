word = input("Word: \n")

while word.lower != "exit":
    if word.lower() == word[::-1].lower():
        print("It's a palindrome!\n")
    else:
        print("It's not a palindrome.\n")

    word = input("Word: \n")

print("Thanks for using the Palindrome checker.")