# Python dictionary is an ordered collection of items. 
# It stores elements in key/value pairs.
# Dictionaries use curly braces `{}` to define key-value pairs.
# Each key is unique and maps to a specific value.
# Here, keys are unique identifiers that are associated with each value.

#Create a dictionary in Python
capital_cities = {"USA": "Washington D.C.","France": "Paris","Japan": "Tokyo","India": "New Delhi"}
print(capital_cities)  # Output: {'USA': 'Washington D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'India': 'New Delhi'}

# Keys are "USA", "France", "Japan", and "India"
# Values are "Washington D.C.", "Paris", "Tokyo", and "New Delhi"

# Staff & Patient Records -Key-value pairs for instant lookups
# Staff Directory (ID → Details)
staff = {
    101: {"name": "Dr. Smith", "role": "Cardiologist", "station": "ER"},
    202: {"name": "Nurse Lee", "role": "ICU", "station": "Ward 3B"},
    303: {"name": "Dr. Patel", "role": "Radiologist", "station": "Lab 2"}
}

# Patient Records (ID → Medical History)
patients = {
    "P881": {"name": "John Munae", "allergies": ["Penicillin"], "ward": "ICU"},
    "P882": {"name": "Maria Garcia", "allergies": ["Smoke"], "ward": "Ward 4A"}
}

# Access data
print("Nurse on duty:", staff[202]['name']) 
# Output: Nurse on duty: Nurse Lee
print("Maria's allergies:", patients["P882"]["allergies"])
# Output: Maria's allergies: ['Smoke']
print("Dr. Patel's station:", staff[303]["station"])
# Output: Dr. Patel's station: Lab 2

# Update records

# Add new patient
patients["P883"] = {"name": "Alex Kim", "allergies": ["Latex"], "ward": "ER"}
(print patients)
# Output: {'P881': {'name': 'John Munae', 'allergies': ['Penicillin'], 'ward': 'ICU'},
#          'P882': {'name': 'Maria Garcia', 'allergies': ['Smoke'], 'ward': 'Ward 4A'},
#          'P883': {'name': 'Alex Kim', 'allergies': ['Latex'], 'ward': 'ER'}}


# Dictionary with keys and values of different data types
numbers = {
    "one": 1, # integer
    "two": 2.0, # float
    "three": [3, 3.1, 3.2], # list
    "four": (4, 4.1), # tuple
    "five": {5: "five"} # dictionary
}
print(numbers)
# Output: {'one': 1, 'two': 2.0, 'three': [3, 3.1, 3.2], 'four': (4, 4.1), 'five': {5: 'five'}}

#Adding new key-value pairs
capital_cities= {"USA": "Washington D.C.", "France": "Paris", "Japan": "Tokyo", "India": "New Delhi"}
print(capital_cities)  # Output: {'USA': 'Washington D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'India': 'New Delhi'}

# Add a new country and its capital
capital_cities["Germany"] = "Berlin"  # Add a new country and its capital
print(capital_cities)
# Output: {'USA': 'Washington D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'India': 'New Delhi', 'Germany': 'Berlin'}

# Updating existing key-value pairs
# Changing the value of a dictionary key
student_ID = {111: "John", 112: "Eric", 113: "Raj"}
print ("initial dictionary:", student_ID)
# Output: initial dictionary: {111: 'John', 112: 'Eric', 113: 'Raj'}

# Update the name of student with ID 112
student_ID[112] = "Eric Smith"  # Update the name of student with ID 112
print("Updated dictionary:", student_ID)
# Output: Updated dictionary: {111: 'John', 112: 'Eric Smith', 113: 'Raj'}

# Deleting key-value pairs
# Remove a key-value pair from the dictionary
del student_ID[113]  # Remove the student with ID 113
print("After deletion:", student_ID)
# Output: After deletion: {111: 'John', 112: 'Eric Smith'}
# Clear all key-value pairs from the dictionary

student_ID.clear()  # Clear all key-value pairs from the dictionary
print("After clearing:", student_ID)
# Output: After clearing: {}

# Dictionary methods
capital_cities= {"USA": "Washington D.C.", "France": "Paris", "Japan": "Tokyo", "India": "New Delhi"}
# 1. Copy - Create a shallow copy of the dictionary
capital_cities_copy = capital_cities.copy()  # Create a shallow copy of the dictionary
print("Copy of capital cities:", capital_cities_copy)
# Output: Copy of capital cities: {'USA': 'Washington D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'India': 'New Delhi', 'Germany': 'Berlin'}

# 2. Get - Retrieve the value for a specific key
capital_of_france = capital_cities.get("France")  # Retrieve the capital of France
print("Capital of France:", capital_of_france)
# Output: Capital of France: Paris

# 3. Keys - Get a list of all keys in the dictionary
capital_keys = capital_cities.keys()  # Get a list of all keys in the dictionary
print("Keys in capital cities:", list(capital_keys))
# Output: Keys in capital cities: ['USA', 'France', 'Japan', 'India', 'Germany']

# 4. Values - Get a list of all values in the dictionary
capital_values = capital_cities.values()  # Get a list of all values in the dictionary
print("Values in capital cities:", list(capital_values))
# Output: Values in capital cities: ['Washington D.C.', 'Paris', 'Tokyo', 'New Delhi', 'Berlin']

# 5. Clear - Remove all key-value pairs from the dictionary
capital_cities.clear()  # Clear all key-value pairs from the dictionary
print("After clearing capital cities:", capital_cities)
# Output: After clearing capital cities: {}

# 6. Pop - Remove a specific key-value pair and return the value
capital_cities = {"USA": "Washington D.C.", "France": "Paris", "Japan": "Tokyo", "India": "New Delhi"}
removed_capital = capital_cities.pop("Japan")  # Remove the capital of Japan
print("Removed capital:", removed_capital)
# Output: Removed capital: Tokyo
print("Capital cities after removal:", capital_cities)
# Output: Capital cities after removal: {'USA': 'Washington D.C.', 'France': 'Paris', 'India': 'New Delhi'}

# 7. All - Check if all keys in the dictionary are truthy
all_keys_truthy = all(capital_cities)  # Check if all keys in the dictionary are truthy
print("Are all keys truthy?", all_keys_truthy)
# Output: Are all keys truthy? True

# 8. Any - Check if any key in the dictionary is truthy
any_key_truthy = any(capital_cities)  # Check if any key in the dictionary is truthy
print("Is any key truthy?", any_key_truthy)
# Output: Is any key truthy? True

# 9. Len - Get the number of key-value pairs in the dictionary
capital_cities = {"USA": "Washington D.C.", "France": "Paris", "Japan": "Tokyo", "India": "New Delhi"}
num_pairs = len(capital_cities)  # Get the number of key-value pairs in the dictionary
print("Number of key-value pairs:", num_pairs)
# Output: Number of key-value pairs: 4

# 10. Sorted - Return a new sorted lists

#Dictionary Membership Test
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# Output: True

print (1 in squares)
# Output: True

# 11. Iterating Through A Dictionary
squares = 

