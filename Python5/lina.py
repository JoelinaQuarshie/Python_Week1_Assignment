class Goon:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return(f""{self.name} {self.age} is a dangerous goon!"")

x = Goon ("Yohana",25)
print (x)