test = [[x * i for i in range(1, 11)] for x in range(1,11)]

print(f"{'Multiplication Table':^50}\n")
for i in test:
    for num, ind in zip(i, range(1,11)):
        if ind == 10:
            print(f"{num:>5}")
        else:
            print(f"{num:>5}", end="")

