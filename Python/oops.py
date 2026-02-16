# ---- all about classes and objects ----

print("Q. 1st")
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print("Name is:", self.name, " Age is:", self.age)

st1 = Student("Sunny", 21)
st2 = Student("Sumit", 22) 
st1.info()
st2.info()
# print(st1.info(), st2.info())
# print(st1.name, st1.age, st2.name, st2.age)
print()

print("Q. 2nd")
class Car:
    def __init__(self, brandName, price):
        self.brandName = brandName
        self.price = price
    def details(self):
        print(self.brandName, self.price)

car1 = Car("Porche 911", 1234567)
car1.details()
print()

print("Q. 3rd")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Sunny", 12345)
emp2 = Employee("Sumit", 12345)
print("Name:", emp1.name, " Salary:", emp1.salary)
print("Name:", emp2.name, " Salary:", emp2.salary)
print()

print("Q. 4th")
class Mobile:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def info(self):
        print("Brand:", self.brand, " Model:", self.model)
mob1 = Mobile("Pixel", "Pixel 6a")
mob2 = Mobile("iPhone", "iPhone 17")
mob1.info()
mob2.info()
print()

print("Q. 6th")
class College:
    collegeName = "BBDU"
    def __init__(self, studentName):
        self.studentName = studentName
    def info(self):
        print("College:", self.collegeName, " Student Name:", self.studentName)
stdnt = College("Sunny")
stdnt.info()