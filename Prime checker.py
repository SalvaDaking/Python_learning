"""
This program checks whether the introduced number is prime or not.
And it also prints all prime numbers up to that particular number..
It assumes that an integer is typed. Coded by: Salva.
"""

def prime_numbers(num):
    '''Returns all prime numbers up to a number'''

    primes = [x for x in range(2, num) if all(x % y != 0 for y in range(2, x))]

    print(f"The primes up to the number {num} are:\n{primes}.\n")

def check_prime(number):
    '''Checks whether a number is prime or not.'''

    # prime = False
    divisible = []
    div_text = ", "

    for num in range(2, number):
        if number % num == 0:
            divisible.append(str(num))

    if len(divisible) == 0:
        print(f"The number {number} is prime!\n")
    else:
        print(f"The number {number} is not prime. It's divisible by {div_text.join(divisible)}.\n")

while True:

    number = int(input("Introduce a number to check whether is prime or not (type 0 to quit): \n"))
    if number == 0:
        break
    else:
        check_prime(number)
        prime_numbers(number)

print("Thanks for using the Prime checker.")
