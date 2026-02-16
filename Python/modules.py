# ---- python modules ----
import math
import random
import string
from datetime import datetime, date

# ---- math module ----
print("---- math module ----\n")

print("Q. 1st")
print(math.sqrt(36))
print()

print("Q. 2nd")
print(math.factorial(6))
print()

print("Q. 3rd")
print(math.floor(4.7))
print(math.ceil(4.7))
print()

print("Q. 4th")
print(math.pow(5, 3))
print()

print("Q. 5th")
print(math.fabs(-18))
print()

print("Q. 6th")
print(math.sin(90), math.cos(90), math.tan(90))
print()

print("Q. 7th")
print(math.gcd(36, 60))
print()

print("Q. 8th")
print(math.exp(3))
print()

print("Q. 9th")
print(math.log(1000, 10))
print()

print("Q. 10th")
print(math.radians(180))
print()

# ---- random module ----
print("---- random module ----\n")

print("Q. 1st")
print(random.randint(1, 10))
print()

print("Q. 2nd")
print(random.random())
print()

print("Q. 3rd")
print(random.choice([12,34,32,55,66]))
print()

print("Q. 4th")
list = [1,2,3,4,5]
random.shuffle(list)
print(list)
print()

print("Q. 5th")
print(random.randrange(2, 10))
print()

print("Q. 6th")
print(random.randint(2, 10))
print()

print("Q. 7th")
print(random.randint(1, 6))
print()

print("Q. 8th")
print(random.sample(['apple', 'banana', 'mango', 'grape', 'orange'], 3))
print()

print("Q. 9th")
print(''.join(random.sample(string.ascii_lowercase, 8)))
print()

print("Q. 10th")
print(random.sample(range(1, 20), 4))
print()

# ---- datetime module ----
print("---- datetime module ----\n")

print("Q. 1st")
print(datetime.now())
print()

print("Q. 2nd")
print(date.today())
print()

print("Q. 3rd")
today = date.today()
print(today.year)
print(today.month)
print(today.day)
print()

print("Q. 4th")
now = datetime.now()
print(now.strftime("%A %d %b %Y %I:%M %p"))
print()

print("Q. 5th")
