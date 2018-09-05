import tkinter as tk
'''Challenge: Convert any number to binary without using bin()'''

window = tk.Tk()
window.title("Decimal 2 Binary calculator")

def dec_to_bin(event):
    '''inputs an integer and returns its binary value'''
    number = int(decimal.get())
    binary = ''

    while number > 0:           # number must be a positive integer.
        binary += str(number % 2)   # calculates the binary number
        number = number // 2

    result.config(text=binary[::-1])
    # print(binary[::-1])

tk.Label(window, text="Introduce a positive integer to convert to binary.").grid(row=0, column=1, columnspan=2)
tk.Label(window, text="Decimal: ").grid(row=1, column=0)
decimal = tk.Entry(window)
tk.Label(window, text="to binary: ").grid(row=1, column=2)
result = tk.Message(window)
decimal.grid(row=1, column=1)
result.grid(row=1, column=3)

button = tk.Button(window, text="Convert")
button.grid(row=2, column=1, columnspan=2)
button.focus_force()
button.bind('<Button-1>', dec_to_bin)


# while True:
#
#     number = input("Introduce a number to convert to binary ('q' to quit):\n")

# if number == "q":
#     break       # Finishes the program.
#         try:        # If number is not an integer, prints a warning and asks again
#             dec_to_bin(int(number))
#         except ValueError:
#             print("Please, introduce a positive integer to convert to binary.\n")
    # else:

# print("Thanks for using the 'Decimal to Binary' converter")

tk.mainloop()
