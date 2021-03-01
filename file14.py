# creating a class
# class NewClass:
#     x = 20

# # using object 
# firstObject = NewClass()
# print(firstObject.x)

# creating new class with init built-in and self arg
# class User:
#     def __init__(self, idnumber, age):
#         self.idnumber = idnumber
#         self.age = age

# # creating object
# firstObject = User(55, 25)
# # printing idnumber and age on the screen
# print("The id number =",firstObject.idnumber)
# print("The age =",firstObject.age)        

# creating a function inside the class
class Person:
    def __init__(self, idnumber, age):
        self.idnumber = idnumber
        self.age = age
    # user function
    def userfunction(self):
        print('Hello, my number is:', self.idnumber, "and my age is:", self.age)
# creaing object
firstObject = Person(33, 20)

# call the user function
firstObject.userfunction()

         
