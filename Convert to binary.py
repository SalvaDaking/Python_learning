def dec_to_bin(number):

    binary = ""

    while number > 0:
        binary += str(number % 2)
        number = number // 2

    print(binary[::-1])

while True:

    number = input("Introduce a number to convert to binary ('q' to quit):\n")

    if number == "q": break
    else:
        try:
            dec_to_bin(int(number))
        except ValueError:
            continue

print("Thanks for using the 'Decimal to Binary' converter")