# Diamond pattern program in Python

# user se input lena (rows ka half size)
n = int(input("Enter the number of rows (half diamond size): "))

# upper triangle
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# lower triangle
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
