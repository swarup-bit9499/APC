file = open("student.txt", "w")

file.write("Name: Swarup\n")
file.write("Course: B.Tech CSE\n")
file.write("Year: 2nd Year")

file.close()

print("File created successfully!")

file = open("student.txt", "r")

data = file.read()

print(data)

file.close()

file = open("student.txt", "r")

for line in file:
    print(line.strip())

file.close()

file = open("student.txt", "a")

file.write("\nMarks: 85")

file.close()

print("Data added successfully!")

with open("student.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("File Handling Example")

print("File written successfully!")