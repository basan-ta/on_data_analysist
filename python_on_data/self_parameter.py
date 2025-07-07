class person:
    def __init__(myobject, name, age):
        myobject.name = name 
        myobject.age = age 
    def myfunc(demo):
        print(f"his name is " + demo.name)

p1 = person("suwash", 23)
p1.myfunc()

#set the age of p1 
p1.age = 24
print(f"His age is "+ str(p1.age))

# To delete the object property 

del p1.age

