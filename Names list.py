name_list = []

print("Introduce name, middle name (optional) and surname.")
name = input("Type 'q' when finish.\n")

while name.lower() != "q":

    name = name.split()

    if len(name) > 2:
        name_list.append(f"{name[-1]}, {name[0]} {name[1]}")
    else:
        name_list.append(f"{name[-1]}, {name[0]}")

    name = input("next name ('q' to finish):\n")

for num, item in enumerate(sorted(name_list), 1):
    print(num, item)
