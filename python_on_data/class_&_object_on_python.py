#Create class
class person:
    #Constructor
    def __init__(self, name, age):
        self.name = name 
        self.age = age 


#creating an objefct of class person
p1 = person("Ram", 23)
p2 = person("sudip", 24)
p3 = person("DKC", 24)

#printing the object
print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)

#Creating a class with methods
class person_with_method:
    #Constructor
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    #Method to display person details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

 #Creating objects of class person_with_method
p1 = person_with_method("Ram", 23)
p2 = person_with_method("sudip", 24)
p3 = person_with_method("DKC", 24)          

#Displaying person details using method
p1.display()
p2.display()
p3.display()

class person_with_method_and_function:
    #Constructor
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    #Method to display person details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    #Function to calculate year of birth
    def year_of_birth(self):
        return 2024 - self.age
    
#Creating objects of class person_with_method_and_function
p1 = person_with_method_and_function("Ram", 23)
p2 = person_with_method_and_function("sudip", 24)
p3 = person_with_method_and_function("DKC", 24)     
#Displaying person details using method
p1.display()
p2.display()
p3.display()