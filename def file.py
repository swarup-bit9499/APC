import os

# Function to create directory
def create_directory():
    if not os.path.exists("MyFolder"):
        os.mkdir("MyFolder")
        print("Directory created")
    else:
        print("Directory already exists")


# Function to create file
def create_file():w
    file = open("MyFolder/example.txt", "w")
    file.write("Hello Python!")
    file.close()
    print("File created")


# Function to delete file 
def delete_file():
    if os.path.exists("MyFolder/example.txt"):
        os.remove("MyFolder/example.txt")
        print("File deleted")


# Function to delete directory
def delete_directory():
    if os.path.exists("MyFolder"):
        os.rmdir("MyFolder")
        print("Directory deleted")


# Calling functions
create_directory()
create_file()
delete_file()
delete_directory()