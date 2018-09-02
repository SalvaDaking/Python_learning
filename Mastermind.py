import random

secret = ["A", "B", "C", "D", "E", "F"]
random.shuffle(secret)
result = ["X"] * 6
tries = 4
show = "".join(secret)

user_code = input("Solve the code [ABCDEF]:\n").upper()

while tries != 0:

    for user, letter, num in zip(user_code, secret, range(0, 6)):
        if user == letter:
            result[num] = "O"
        else:
            result[num] = "X"

    print("".join(result))

    if "".join(secret) == "".join(user_code):
        print("Well done!! You solved the code.")
        break

    tries -= 1

    user_code = input(f"next try {tries} left:\n").upper()

if tries == 0:
    print("I'm sorry but you don't have more tries.")
    print(f"The code was {show}.")

print("Thanks for playing.")
