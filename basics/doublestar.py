n = int(input("Enter number of rows: "))

stars = ""  # string banayenge

# increasing stars
for i in range(1, n + 1):
    stars += "*" * i + "\n"

# decreasing stars
for i in range(n - 1, 0, -1):
    stars += "*" * i + "\n"

print(stars)
