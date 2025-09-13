# String Indexing Example in Python

# User se input lena
text = input("Enter a string: ")

print("\nOriginal String:", text)
print("Length of String:", len(text))

print("\nPositive Indexing (Left to Right):")
for i in range(len(text)):
    print(f"Index {i} -> {text[i]}")

print("\nNegative Indexing (Right to Left):")
for i in range(-1, -len(text)-1, -1):
    print(f"Index {i} -> {text[i]}")
