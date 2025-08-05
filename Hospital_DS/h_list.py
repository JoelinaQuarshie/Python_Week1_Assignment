# Hospital Ward Management List - Ordered collections for patient beds
# Ward 4A Patient Beds (Ordered by proximity to nurses' station)
ward_4a = ["Bed1: Robert", "Bed2: Fatima", "Bed3: James"]

# New admission
ward_4a.append("Bed4: Aisha")
ward_4a.insert(2, "Bed5: Liam")  # Insert a new bed at the 3rd position
print("Ward 4A:", ward_4a)  
# Output: ['Bed1: Robert', 'Bed2: Fatima', 'Bed5: Liam', 'Bed3: James', 'Bed4: Aisha']
ward_4a.remove("Bed1: Robert")  # Remove a specific bed
print("After removal:", ward_4a)

# Output: ['Bed1: Robert', 'Bed2: Fatima', 'Bed3: James', 'Bed4: Aisha']


# Discharge patient
discharged = ward_4a.pop(2) # Discharge the patient in Bed3
print(f"Discharged: {discharged} → Remaining: {ward_4a}")  
# Output: Discharged: Bed3: James → Remaining: ['Bed2: Fatima', 'Bed5: Liam', 'Bed4: Aisha']

