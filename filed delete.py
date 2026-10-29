import os

# Delete file if it exists
if os.path.exists("MyFolder/example.txt"):
    os.remove("MyFolder/example.txt")
    print("File deleted")

# Delete directory if it exists
if os.path.exists("MyFolder"):
    os.rmdir("MyFolder")
    print("Directory deleted")

# Create directory
os.mkdir("MyFolder")
print("Directory created")

# Create file
file = open("MyFolder/example.txt", "w")
file.write("Hello Python!")
file.close()

print("File created")