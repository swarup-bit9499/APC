import os

# Create directory
os.mkdir("MyFolder")
print("Directory created")

# Create file
file = open("MyFolder/example.txt", "w")
file.write("Hello Python!")
file.close()
print("File created")

# Delete file
os.remove("MyFolder/example.txt")
print("File deleted")

# Delete directory
os.rmdir("MyFolder")
print("Directory deleted")