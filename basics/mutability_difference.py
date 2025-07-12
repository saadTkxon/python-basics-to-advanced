
# Difference Between Mutable and Immutable


print(" Mutable vs Immutable - Simple Difference\n")

# #  Immutable Data Types
# # These cannot be changed after creation

immutable_types = ["int", "float", "bool", "str", "tuple", "frozenset", "bytes"]

print(" Immutable Data Types:")
for item in immutable_types:
    print(f" - {item} (Can't be changed after creation)")

# Example:
num = 5
print("\nExample:")
print("num =", num)
print("Changing num to 10...")
num = 10  # Creates a new object
print("Updated num =", num)


# #  Mutable Data Types
# # These can be changed after creation

mutable_types = ["list", "dict", "set", "bytearray"]

print("\n Mutable Data Types:")
for item in mutable_types:
    print(f" - {item} (Can be changed after creation)")

# Example:
my_list = [1, 2, 3]
print("\nExample:")
print("my_list =", my_list)
print("Changing first item of my_list to 100...")
my_list[0] = 100  # Modifies the original list
print("Updated my_list =", my_list)


# #  Summary Table (Text Format)

print("\n==============================")
print(" Summary: Mutability Table")
print("==============================")
print("| Data Type   | Mutable?     |")
print("|-------------|--------------|")
print("| int         |  No        |")
print("| float       |  No        |")
print("| str         |  No        |")
print("| tuple       |  No        |")
print("| list        |  Yes       |")
print("| dict        |  Yes       |")
print("| set         |  Yes       |")
print("==============================")
