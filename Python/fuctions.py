print("\n# 1st")
def printHello():
    print("Hello, Python")
printHello()

print("\n# 2nd")
name = input("Enter name: ")
def greet(name):
    print("Hello, ", name)
greet("Sunny")

print("\n# 3rd")
num1 = (int) (input("Enter num1: "))
num2 = (int) (input("Enter num2: "))
def sum(x, y):
    print("Sum is: ", x + y)
sum(num1, num2)

print("\n# 4th")
def square(x):
    print("Square is: ", x ** 2)
square(num1)

print("\n# 5th")
def evenOdd(x):
    if (x % 2 == 0):
        print("Even")
    else:
        print("Odd")

print("\n# 6th")
def maximum(x, y):
    if (x > y):
        return x
    else:
        return y
print(maximum(num1, num2))

print("\n# 7th")
list = (12, 54, 3, 6, 7, 54, 32, 21)
def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)
print(average(list))

print("\n# 8th")
str = "aekhjuia"
def countVowel(str):
    count = 0
    for i in str:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
            or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            count += 1
    return count
