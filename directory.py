import os

os.mkdir("MyFolder")

print("Directory created successfully!")

import os

if os.path.exists("MyFolder"):
    print("Directory exists")
else:
    print("Directory does not exist")

import os

items = os.listdir(".")

for item in items:
    print(item)

    import os

os.mkdir("MyFolder")

with open("MyFolder/example.txt", "w") as file:
    file.write("This file is inside MyFolder.")

print("File created!")

import os

os.rename("student.txt", "student_data.txt")

print("File renamed successfully!")