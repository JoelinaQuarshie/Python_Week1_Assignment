PLP = "Academy"

Student_Name = "Joelina Quarshie"

Student_ID = 1001

Student_Age = 20.2

Fee_Clearance = True
# True means fees are cleared, False means not cleared

print(Student_Name, Student_ID, Fee_Clearance)

#Lists (mutable, uses square brackets)
languages = [1995, "Python", "Java", "C++", "JavaScript"]
print(languages)

shopping_list = ["Rice", "Beans", "Eggs", "Milk", "Bread" ,"Butter"]
print(shopping_list)

# Tuples (immutable,uses parentheses)
products = ('XBox', 499.99, "Habibi", 23)
print(products)

# data set (mutable, unordered, no duplicates, uses curly brackets)
student_ids = {112, 114, 117, 113}
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}
print(set_A)
print(set_B)

# Dictionary (mutable, unordered, uses curly brackets)
student_info = {"Name": "Joelina Quarshie", "ID": 1001, "Age": 20.2, "Fee Clearance": True}
print(student_info)

capital_citys = {"Ghana": "Accra", "Nigeria": "Abuja", "Kenya": "Nairobi", "South Africa": "Capetown"}
print(capital_citys)

# Logical Operators
a = 10
b = 20
c = 30
print(a < b and b < c)  # True
print(a < b or b > c)   # True
print(not (a < b))       # False