#Sets
#In Python, we create sets by placing all the elements inside curly braces {}, separated by comma.
#A set can have any number of items and they may be of different types (integer, float, tuple, string etc.). 
# But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

#Example
#Equipment Tracking & Sterilization -Unique items for contamination control
# Sterilized equipment sets
sterile_lab_equipment = {"Microscope", "Centrifuge", "Pipettes"}
sterile_er_equipment = {"Stethoscope", "Defibrillator", "Sutures"}

# Contaminated items
contaminated = {"Defibrillator", "Sutures", "Scalpel"}

# Sterilize ER equipment
sterile_er_equipment -= contaminated
print("Sterile ER Equipment:", sterile_er_equipment)  
# Output: {'Stethoscope'}

print(contaminated)
# Output: {'Defibrillator', 'Sutures', 'Scalpel'}

# Combine all sterile tools
all_sterile = sterile_lab_equipment | sterile_er_equipment
print("All Sterile Equipment:", all_sterile)  
# Output: {'Microscope', 'Centrifuge', 'Pipettes', 'Stethoscope'}

#Empty Set
#empty_set - an empty set created using set()
#empty_dictionary - an empty dictionary created using {}