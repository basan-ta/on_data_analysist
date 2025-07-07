class person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
#The string representation of an object WITH the __str__() function
        def __str__(self):
            return f"Name: {self.name}, Age: {self.age}"
p1 = person("suwash", 23)
p2 = person("sudip", 24)
p3 = person("DKC", 24)

print(p1) 
print(p2)  
