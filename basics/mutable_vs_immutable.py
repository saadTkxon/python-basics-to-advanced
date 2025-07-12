#
#  Python Mutability: Basics with Variables
#

#
#  Immutable Data Types
#

# Immutable types cannot be changed after they are created.
# These include: int, float, bool, str, tuple, frozenset

print("------ IMMUTABLE EXAMPLES ------")

# Integer (int) is immutable
a = 10
print("Original a:", a)
a = 20  # A new value is assigned. Old 10 is not changed, it's replaced.
print("Modified a:", a)

# String (str) is immutable
name = "Saad"
print("Original name:", name)
name = name + " tkxon"  # This creates a new string, doesn't change the original
print("Modified name:", name)

# Tuple is immutable
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)
# my_tuple[0] = 99  #  This will give an error because tuples can't be modified


#
#  Mutable Data Types
#

# Mutable types can be changed after they are created.
# These include: list, dict, set, bytearray

print("\n------ MUTABLE EXAMPLES ------")

# List is mutable
my_list = [1, 2, 3]
print("Original list:", my_list)
my_list[0] = 99  #  This changes the first item in the list
print("Modified list:", my_list)

# Dictionary is mutable
my_dict = {"name": "Saad", "age": 25}
print("Original dictionary:", my_dict)
my_dict["age"] = 26  #  Updating the value of a key
print("Modified dictionary:", my_dict)

# Set is mutable
my_set = {1, 2, 3}
print("Original set:", my_set)
my_set.add(4)  #  Adds a new element to the set
print("Modified set:", my_set)


#
#  Summary
#
#  Immutable types = Can't change the object (new value = new object)
#  Mutable types = Can modify the object itself

# You can use `id()` to see if a new object was created
x = "Hello"
print("\nID before:", id(x))
x += " World"
print("ID after:", id(x))  # New ID means a new object was created

y = [1, 2, 3]
print("\nID before (list):", id(y))
y.append(4)
print("ID after (list):", id(y))  # Same ID means the same object was modified
