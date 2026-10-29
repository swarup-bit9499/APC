import os

# Create directory only if it doesn't exist
if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")
    print("Directory created")
else:
    print("Directory already exists")

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