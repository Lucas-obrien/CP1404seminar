# infile = open("readme.txt", "r")
#
# for line in infile:
#     if line[0] == "#":
#         print(line.strip())
#
# infile.close()

with open("guitar.txt", "r") as in_file:
    for line in in_file:
        parts = line.strip().split(",")
        guitar = parts[0]
        year = parts[1]
        price = parts[2]

        print(f"{guitar}; year made: {year}; value is ${price}")
