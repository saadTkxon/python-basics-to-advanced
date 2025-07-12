
#  Basic Python Data Types with Simple Examples


print(" Python Basic Data Types\n")

#
#  1. Integer (int)
# Whole numbers, positive or negative
x = 10
print("Integer (int):", x)

#
#  2. Float (float)
# Decimal numbers
pi = 3.14
print("Float (float):", pi)

#
#  3. Boolean (bool)
# True or False values
is_active = True
print("Boolean (bool):", is_active)

#
#  4. String (str)
# Text or characters inside quotes
name = "Saad"
print("String (str):", name)

#
#  5. List (list)
# Ordered, mutable collection (can change)
my_list = [1, 2, 3, "hello"]
print("List (list):", my_list)

#
#  6. Tuple (tuple)
# Ordered, immutable collection (cannot change)
my_tuple = (10, 20, 30)
print("Tuple (tuple):", my_tuple)

#
#  7. Dictionary (dict)
# Key-value pairs, unordered, mutable
my_dict = {
    "name": "Saad",
    "age": 25
}
print("Dictionary (dict):", my_dict)

#
#  8. Set (set)
# Unordered collection with unique values
my_set = {1, 2, 3, 3, 4}
print("Set (set):", my_set)  # Duplicate 3 is removed automatically

#
# 9. Bytes (bytes)
# Immutable binary data
my_bytes = b"Hello"
print("Bytes (bytes):", my_bytes)

#
#  10. Bytearray (bytearray)
# Mutable binary data
my_bytearray = bytearray(b"Hello")
print("Bytearray (bytearray):", my_bytearray)

#
#  11. NoneType (None)
# Represents no value or null
nothing = None
print("NoneType (None):", nothing)


# ==========================
#  Summary Table
# ==========================

print("\n==============================")
print(" Python Data Types Summary")
print("==============================")
print("| Type        | Example           |")
print("|-------------|-------------------|")
print("| int         | 10                |")
print("| float       | 3.14              |")
print("| bool        | True              |")
print("| str         | 'Hello'           |")
print("| list        | [1, 2, 3]         |")
print("| tuple       | (1, 2, 3)         |")
print("| dict        | {'a': 1}          |")
print("| set         | {1, 2, 3}         |")
print("| bytes       | b'Hello'          |")
print("| bytearray   | bytearray(b'Hi')  |")
print("| NoneType    | None              |")
print("==============================")
