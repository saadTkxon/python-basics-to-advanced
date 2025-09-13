# String Full Operations Example

# Take input
text = input("Enter a string: ")

print("\nOriginal String:", text)
print("Length of String:", len(text))

# -------------------------------
# Indexing
# -------------------------------
print("\n--- Indexing ---")
print("First character (text[0]):", text[0])
print("Last character (text[-1]):", text[-1])
print("Character at index 2:", text[2])

# -------------------------------
# Slicing
# -------------------------------
print("\n--- Slicing ---")
print("text[0:3]  ->", text[0:3])   # First 3 chars
print("text[2:5]  ->", text[2:5])   # From index 2 to 4
print("text[:4]   ->", text[:4])    # From start to index 3
print("text[3:]   ->", text[3:])    # From index 3 to end
print("text[-3:]  ->", text[-3:])   # Last 3 chars
print("text[::-1] ->", text[::-1])  # Reverse string

# -------------------------------
# Updating (replace character by index)
# -------------------------------
print("\n--- Updating ---")
# Strings immutable hain, so convert to list
text_list = list(text)
print("Original as list:", text_list)

# Example: Replace 1st char
text_list[0] = "Z"
updated_text = "".join(text_list)
print("After updating 1st char ->", updated_text)

# Example: Replace middle char
if len(text_list) > 3:
    text_list[3] = "X"
    updated_text = "".join(text_list)
    print("After updating index 3 ->", updated_text)

# -------------------------------
# Deleting (remove character by index)
# -------------------------------
print("\n--- Deleting ---")
text_list = list(text)
print("Original as list:", text_list)

# Example: Delete 2nd char
del text_list[1]
deleted_text = "".join(text_list)
print("After deleting index 1 ->", deleted_text)

# Example: Delete last char
text_list = list(text)  # reset
del text_list[-1]
deleted_text = "".join(text_list)
print("After deleting last char ->", deleted_text)
