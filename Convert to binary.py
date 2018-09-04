'''Challenge: Convert any number to binary without using bin()'''

def dec_to_bin(number:int) -> bin:
    '''inputs an integer and returns its binary value'''

    binary = ''

    while number > 0:           # number must be a positive integer.
        binary += str(number % 2)   # calculates the binary number
        number = number // 2

    print(binary[::-1])

while True:

    number = input("Introduce a number to convert to binary ('q' to quit):\n")

    if number == "q":
        break       # Finishes the program.
    else:
        try:        # If number is not an integer, prints a warning and asks again
            dec_to_bin(int(number))
        except ValueError:
            print("Please, introduce a positive integer to convert to binary.\n")

print("Thanks for using the 'Decimal to Binary' converter")