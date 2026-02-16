with open("test.txt", "w") as file:
    file.write("Hello, Python\nsecond line ")
with open("test.txt", "r") as file:
    print(file.read())
    
with open("/Users/sunny/dev/python/test2.txt", "rb") as file:
    print(file.read())
    
with open("/Users/sunny/dev/python/assign-I/WhatsApp Image 2026-01-18 at 20.11.59.jpeg", "rb") as file:
    print(file.read())