'''
get number of gifts
get number of students

display number of students / number of gifts
display number of students % number of gifts

'''

# number_of_gifts = int(input("Number of gifts: "))
# number_of_students = int(input("Number of students: "))
#
# number_of_gifts_per_student = number_of_gifts // number_of_students
# number_of_gifts_leftover = number_of_gifts % number_of_students
#
# print(f"gifts per student is {number_of_gifts_per_student}")
# print(f"Left over gifts: {number_of_gifts_leftover}")

GST_RATE = 1.10

item_price = float(input("Item price: $"))

if input("Does this have GST? Y/n: ").upper() == "Y":
    item_price = item_price * GST_RATE

print(f"Final price is : ${item_price:.2f}")
