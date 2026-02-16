# [ : : -1]
# --- Lists ----

print("# 1st \n")
list = [1, 2, 3, 4, 5, 5, 6]
print(list[0])
print(list[len(list) - 1])
print(len(list))

print("# 2nd \n")
sum = 0
for i in list:
    sum += i
print("Sum: ", sum, "Average: ", sum / len(list))

print("# 3rd \n")
fruits = ["apple", "mango", "banana", "strawberry", "apple"]
print(fruits.append("craneberry"))
print(fruits.insert(2, "avocado"))

print("# 4th \n")
list.remove(4)
list.pop()

print("# 5th \n")
print(list.count(5))

# ---- Searching & Sorting ----

print("# 6th \n")
flag = True
for i in list:
    if (8 == i):
        flag = True
        break
    else:
        flag = False
if (flag):
    print("Exist")
else:
    print("Does not exist")

print("# 7th \n")
print(list.index(5))


