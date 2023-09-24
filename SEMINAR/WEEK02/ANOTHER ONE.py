# import random
#
# high_number = int(input("enter a high number: "))
# low_number = int(input("enter a low number: "))
# while low_number >= high_number:
#     print(f"low number must be lower than {high_number}")
#     low_number = int(input("enter a low number: "))
#
# print(":)" * (random.randint(low_number, high_number)))

def main():
    print(is_even(2))
    print(is_even(3))


def is_even(number):
    return number % 2 == 0


main()
