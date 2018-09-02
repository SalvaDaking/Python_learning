while True:

    result = 1

    numbers = input("Introduce a list of numbers separated by comma (,) or type q to quit:\n")

    if numbers.lower() == "q":
        break

    num_list = numbers.split(",")

    for num in num_list:
        result *= int(num)

    print(result)

print("Thanks for using the list multiplicator.")
