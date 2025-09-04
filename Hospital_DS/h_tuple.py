#Tuples
# A tuple is created by placing all the items (elements) inside parentheses (), separated by commas. The parentheses are optional, however, it is a good practice to use them.
# A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).
# Tuples are immutable, meaning once created, their values cannot be changed.
# Like a list, each element of a tuple is represented by index numbers (0, 1, ...) where the first element is at index 0.

# Creating a tuple with one item requires a trailing comma to distinguish it from a regular parenthesis.
# Example
# Creating a tuple with one item
single_item_tuple = (42,)  # A tuple with one item
print("Single Item Tuple:", single_item_tuple)  
# Output: Single Item Tuple: (42,)

# Creating a tuple with multiple items
multiple_items_tuple = (1, 2, 3, "Hello", 4.5)  # A tuple with multiple items
print("Multiple Items Tuple:", multiple_items_tuple)
# Output: Multiple Items Tuple: (1, 2, 3, 'Hello', 4.5)

# Accessing tuple elements
#Indexing similar to lists.
#The index must be an integer, so we cannot use float or other types. This will result in TypeError.

# Accessing elements by index
letters = (p,r,o,g,r,a,m,m,i,n,g)
print(letters[0])  # Accessing the first element
# Output: p
print(letters[3])  # Accessing the fourth element
# Output: g

# Negative indexing to access elements from the end
print(letters[-1])  # Accessing the last element
# Output: g
print(letters[-2])  # Accessing the second last element
# Output: n

#Python tuple methods
#1. Count-Count how many times a specific item appears in the tuple
count_letters = letters.count("g")  # Count how many times 'g' appears
print(count_letters)
# Output: 2

#2. Index-Find the index of a specific item
index_letters = letters.index("r")  # Find the index of the first occurrence of 'r'
print(index_letters)
# Output: 1

#3. Copy-Create a shallow copy of the tuple
letters_copy = letters  # Tuples are immutable, so this creates a reference, not a copy
print(letters_copy)
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g')

#4. Join-Combine multiple tuples into one
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2  # Combine two tuples
print(combined_tuple)
# Output: (1, 2, 3, 4, 5, 6)

letters = (p,r,o,g,r,a,m,m,i,n,g)

#5. Slice-Extract a portion of the tuple
sliced_tuple = letters[2:5]  # Extract elements from index 2 to 4
print(sliced_tuple)
# Output: ('o', 'g', 'r')

#6. Iterate-Loop through the tuple
print("Letters in the tuple:")
for letter in letters:
    print(letter, end='.') # Print each letter in the tuple
# Output: Letters in the tuple:
# p.r.o.g.r.a.m.m.i.n.g.

#7. Nested Tuples-Tuples within tuples. Each tuple is a separate element called a section.
# Each section can have its own items, and they can be of different types.
# Example of nested tuples
nested_tuple = (("A", "B"), ("C", "D"), ("E", "F"))
print("Nested Tuple Elements:")
for section in nested_tuple:
    for item in section:
        print(item, end=' ')
# Output: Nested Tuple Elements:
# A B C D E F


#Example of using tuples in a hospital context
# Hospital Emergency Exit Locations -Nested tuples for complex data
# Emergency Exit Locations (Floor, X, Y)
emergency_exits = (#section 0 
    ("Main Lobby", 1, 12.5),
    #item(0),item(1),item(2)

    #section 1
    ("ER Back", 1, 87.3),
    #item(0),item(1),item(2)

    #section 2
    ("ICU Wing", 3, 45.0) 
    #item(0),item(1),item(2)
)

# Accessing elements in nested tuples
print(emergency_exits[0][0])  # Accessing the first section's name and first item
# Output: Main Lobby

print(emergency_exits[1][2])  # Accessing the second section's Y coordinate(third item)
# Output: 87.3

print(emergency_exits[1][0])  # Accessing the second section's name and first item
# Output: ER Back

print(emergency_exits[1][1])  # Accessing the second section's X coordinate(second item)
# Output: 1

print(emergency_exits[2][0])  # Accessing the third section's name and first item
# Output: ICU Wing

#The index must be an integer, so we cannot use float or other types. This will result in TypeError.
# Try to modify (will fail)
try:
    emergency_exits[1] = ("Lab Zone", 2, 33.1)
except TypeError as e:
    print("Security Alert! ", e) 
    # Output: 'tuple' object does not support item assignment

#Python tuple comprehension
#Tuple comprehension is similar to list comprehension, but it creates a tuple instead of a list.
# It allows you to create a tuple in a concise way, especially when filtering or transforming data.
# Tuple comprehension is not a built-in feature in Python, but you can achieve similar functionality using generator expressions and the `tuple()` constructor.

# Example of tuple comprehension
squared_numbers = tuple(x**2 for x in range(5))  # Create a tuple of squared numbers
print(squared_numbers)
# Output: (0, 1, 4, 9, 16)

# Example of tuple comprehension with a condition
even_squared_numbers = tuple(x**2 for x in range(10) if x % 2 == 0)  # Create a tuple of squared even numbers
print(even_squared_numbers)
# Output: (0, 4, 16, 36, 64)

#Python tuple unpacking
#Tuple unpacking allows you to assign the elements of a tuple to multiple variables in a single
#statement. This is useful when you want to extract values from a tuple and assign them to individual variables.

# Example of tuple unpacking
# Unpacking a tuple into variables
person = ("Alice", 30, "Engineer")  # A tuple with name, age, and profession
name, age, profession = person  # Unpacking the tuple into variables
print(f"Name: {name}, Age: {age}, Profession: {profession}")
# Output: Name: Alice, Age: 30, Profession: Engineer


# Tuple unpacking can also be used with nested tuples
# Example of tuple unpacking with nested tuples
nested_person = (("Alice", "Smith"), 30, "Engineer")  # A tuple with nested name, age, and profession
(first_name, last_name), age, profession = nested_person  # Unpacking the nested tuple
print(f"First Name: {first_name}, Last Name: {last_name}, Age: {age}, Profession: {profession}")
# Output: First Name: Alice, Last Name: Smith, Age: 30, Profession: Engineer


# Example of tuple unpacking with nested tuples in a hospital context
# Hospital Staff Information -Tuple unpacking for structured data
staff_info = (
    ("Dr. Smith", "Cardiologist", "ER"),
    ("Nurse Lee", "ICU", "Ward 3B"),
    ("Dr. Patel", "Radiologist", "Lab 2")
)
# Unpacking staff information
for staff in staff_info:
    name, role, station = staff  # Unpacking each staff member's information
    print(f"Name: {name}, Role: {role}, Station: {station}")
# Output:
# Name: Dr. Smith, Role: Cardiologist, Station: ER
# Name: Nurse Lee, Role: ICU, Station: Ward 3B
# Name: Dr. Patel, Role: Radiologist, Station: Lab 2

#Python Tuple Methods
# Tuples have limited methods compared to lists, but they do have some useful ones.

emergency_exits = (
    ("Main Lobby", 1, 12.5),
    ("ER Back", 1, 87.3),
    ("ICU Wing", 3, 45.0) 
)

#1. Count-Count how many times a specific item appears in the tuple
count_bed = emergency_exits.count(("ER Back", 1, 87.3))  # Count how many times a specific exit appears
print(count_bed)
# Output: 1

#2. Index-Find the index of a specific item
index_bed = emergency_exits.index(("ICU Wing", 3, 45.0))  # Find the index of a specific exit
print(index_bed)
# Output: 2

#3. Copy-Create a shallow copy of the tuple
emergency_exits_copy = emergency_exits  # Tuples are immutable, so this creates a reference, not a copy
print(emergency_exits_copy)
# Output: (('Main Lobby', 1, 12.5), ('ER Back', 1, 87.3), ('ICU Wing', 3, 45.0))

#4. Join-Combine multiple tuples into one
combined_exits = emergency_exits + (("Lab Zone", 2, 33.1),)  # Combine two tuples
print(combined_exits)
# Output: (('Main Lobby', 1, 12.5), ('ER Back', 1, 87.3), ('ICU Wing', 3, 45.0), ('Lab Zone', 2, 33.1))

emergency_exits = (
    ("Main Lobby", 1, 12.5),
    ("ER Back", 1, 87.3),
    ("ICU Wing", 3, 45.0) 
)

#5. Slice-Extract a portion of the tuple
sliced_exits = emergency_exits[1:3]  # Extract exits from index 1 to 2
print(sliced_exits)
# Output: (('ER Back', 1, 87.3), ('ICU Wing', 3, 45.0))

#6. Iterate-Loop through the tuple
print("Emergency Exits:")
for exit in emergency_exits:
    print(f"Exit: {exit[0]}, Floor: {exit[1]}, X: {exit[2]}")
# Output:
# Emergency Exits:
# Exit: Main Lobby, Floor: 1, X: 12.5
# Exit: ER Back, Floor: 1, X: 87.3
# Exit: ICU Wing, Floor: 3, X: 45.0

