# ---- sets ----
print("# 1st")
colors = {"red", "blue", "green"}
print(colors)

print("\n# 2nd")
nums = {12, 34, 45, 45, 69}
print(nums)

print("\n# 3rd")
for i in nums:
    print(i, end=" ")

print("\n# 4th")
set = {"sunny", 17, "bbdu", 6.5}
set.add("btech")
print(set)

print("\n# 5th")
set.remove("bbdu")
print(set)

print("\n# 6th")
set.discard(6.5)
print(set)

print("\n# 7th")
set.pop()
print(set)
