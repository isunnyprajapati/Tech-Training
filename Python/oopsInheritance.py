"""class Animal:
    def sound(self):
        print("Animal make sounds")
        
class Cat(Animal):
    def sound(self):
        print("Meow!")
a = Animal()
c = Cat()
a.sound()
c.sound()"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # Private attribute
        
    def deposit(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance
acc = BankAccount("Alice", 10000)
acc.deposit(5000)
print(acc.get_balance())
print()

# ---- Questions ----
print("Q. 1st")
class Student:
    def __init__(self, name, rollNo, marks):
        self.name = name
        self.rollNo = rollNo
        self.marks = marks

st1 = Student("Sunny", 17, 40)
print("Name:", st1.name, "  Roll No.:", st1.rollNo, "  Marks:", st1.marks)
print()

print("Q. 2nd")
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def areaOfCircle(self):
        return (3.14 * self.radius ** 2)
    def circumference(self):
        return (2 * 3.14 * self.radius)

circle = Circle(5)
print("Area", circle.areaOfCircle())
print("Circumference:", circle.circumference())
print()

print("Q. 3rd")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def displayDetails(self):
        print("Name:", self.name, "  Age:", self.age, "  Salary:", self.salary)
        
emp = Employee("Sunny", 21, 1500000)
emp.displayDetails()
print()

print("Q. 4th")
class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    def drive(self):
        print("Driving the vehicle")
car = Car()
car.start()
car.drive()
print()

print("Q. 5th")
class Grandfather:
    def show(self):
        print("Grandfather class")
class Father(Grandfather):
    def show(self):
        print("Father class")
class Son(Father):
    def show(self):
        print("Son class")
grandfather = Grandfather()
grandfather.show()
father = Father()
father.show()
son = Son()
son.show()
print()

print("Q. 6th")
class Teacher:
    def show(self):
        print("Teacher class")
class Student:
    def show(self):
        print("Student class")
class TeachingAssistant(Teacher, Student):
    def display(self):
        Teacher.show(self)
        Student.show(self)
ta = TeachingAssistant()
ta.display()
print()

print("Q. 7th")
class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        print("Dog sound")
class Cat(Animal):
    def sound(self):
        print("Cat sound")
dog = Dog()
dog.sound()
cat = Cat()
cat.sound()
print()

print("Q. ")