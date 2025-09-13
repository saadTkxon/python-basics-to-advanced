n = int(input("Enter number of rows: "))

stars = ""  # string banayenge

for i in range(1, n + 1):
    stars += "*" * i + "\n"   # har row me i stars

print(stars)
