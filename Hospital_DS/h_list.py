# Hospital Ward Management List - Ordered collections for patient beds
# Ward 4A Patient Beds (Ordered by proximity to nurses' station)
# Lists use square brackets
ward_4a = ["Bed1: Robert", "Bed2: Fatima", "Bed3: James"]

#Adding and removing elements to a list
# New admission
#1.Append-Add a new bed at the end
ward_4a.append("Bed4: Aisha")  # Add a new bed at the end
print("Ward 4A:", ward_4a)  
# Output: ['Bed1: Robert', 'Bed2: Fatima', 'Bed3: James', 'Bed4: Aisha']

#2.Insert-Add a new bed at a specific position
ward_4a.insert(2, "Bed5: Liam")  # Insert a new bed at the 3rd position
print("Ward 4A:", ward_4a)  
# Output: ['Bed1: Robert', 'Bed2: Fatima', 'Bed5: Liam', 'Bed3: James', 'Bed4: Aisha']

#3.Remove a patient(exempt from list)
ward_4a.remove("Bed1: Robert")  # Remove a specific bed
print("After removal:", ward_4a)

# Output: ['Bed1: Robert', 'Bed2: Fatima', 'Bed3: James', 'Bed4: Aisha']

#4. Pop- Delete a specific element and return it
# Pop removes the last element by default, but can also remove a specific index
# Discharge patient
discharged = ward_4a.pop(2) # Discharge the patient in Bed3
print(f"Discharged: {discharged} → Remaining: {ward_4a}")  
# Output: Discharged: Bed3: James → Remaining: ['Bed2: Fatima', 'Bed5: Liam', 'Bed4: Aisha']

#5. Clear-Empty the entire list
ward_4a.clear()  # Clear all beds in the ward
print("Ward 4A after clearing:", ward_4a)
# Output: Ward 4A after clearing: []    

#6. Sort-Organize beds alphabetically
ward_4a = ["Bed3: James", "Bed1: Robert", "Bed  2: Fatima"]
ward_4a.sort()  # Sort beds alphabetically
print("Sorted Ward 4A:", ward_4a)
# Output: Sorted Ward 4A: ['Bed1: Robert', 'Bed2: Fatima', 'Bed3: James']

#7. Reverse-Change the order of beds
ward_4a.reverse()  # Reverse the order of beds
print("Reversed Ward 4A:", ward_4a)
# Output: Reversed Ward 4A: ['Bed3: James', 'Bed2: Fatima', 'Bed1: Robert']

#8.Extend-Add multiple beds at once
new_beds = ["Bed5: Liam", "Bed6: Aisha"]
ward_4a.extend(new_beds)  # Add multiple beds at once
print("Ward 4A after extending:", ward_4a)
# Output: Ward 4A after extending: ['Bed3: James', 'Bed2: Fatima', 'Bed1: Robert', 'Bed5: Liam', 'Bed6: Aisha']

ward_4a = ["Bed1: Robert", "Bed2: Fatima", "Bed3: James"]
additional_beds = ["Bed4: Aisha", "Bed5: Liam"]

#9. Count-Count occurrences of a specific bed
count_bed = ward_4a.count("Bed1: Robert")  # Count how many times a specific bed appears
print("Count of Bed1: Robert:", count_bed)
# Output: Count of Bed1: Robert: 1

#10. Index-Find the index of a specific bed
index_bed = ward_4a.index("Bed2: Fatima")  # Find the index of a specific bed
print("Index of Bed2: Fatima:", index_bed)
# Output: Index of Bed2: Fatima: 1

#11. Copy-Create a shallow copy of the list
ward_4a_copy = ward_4a.copy()  # Create a shallow copy of the list
print("Copy of Ward 4A:", ward_4a_copy)
# Output: Copy of Ward 4A: ['Bed1: Robert', 'Bed2: Fatima', 'Bed3: James']

#12. Join-Combine multiple lists into one
additional_beds = ["Bed4: Aisha", "Bed5: Liam"]
ward_4a_combined = ward_4a + additional_beds  # Combine two lists
print("Combined Ward 4A:", ward_4a_combined)
# Output: Combined Ward 4A: ['Bed1: Robert', 'Bed2: Fatima', 'Bed3: James', 'Bed4: Aisha', 'Bed5: Liam']

#13. Slice-Extract a portion of the list
ward_4a_slice = ward_4a[1:3]  # Extract beds from index 1 to 2
print("Sliced Ward 4A:", ward_4a_slice)
# Output: Sliced Ward 4A: ['Bed2: Fatima', 'Bed3: James']

#14. Iterate-Loop through the list
print("Beds in Ward 4A:")
for bed in ward_4a:
    print(bed)
# Output: Beds in Ward 4A:
# Bed1: Robert
# Bed2: Fatima
# Bed3: James

#15. Nested Lists-Lists within lists
nested_ward = [["Bed1: Robert", "Bed2: Fatima"], ["Bed3: James", "Bed4: Aisha"]]
print("Nested Ward Beds:")
for section in nested_ward:
    for bed in section:
        print(bed) 
# Output: Nested Ward Beds:
# Bed1: Robert
# Bed2: Fatima
# Bed3: James
# Bed4: Aisha


#List Comprehension - Create a new list based on an existing one
#A list comprehension consists of an expression followed by the for statement inside square brackets.
#Here is an example to make a list with each item being increasing by power of 2.
numbers =[number*number for number in range(1, 6)]
print("Numbers squared:", numbers)
# Output: Numbers squared: [1, 4, 9, 16, 25]

numbers =[x*x for x in range(1, 6)]
print(numbers)
# Output: [1, 4, 9, 16, 25]


