#  File I/O — Reading and Writing Files

# Writing to a file
with open("notes.txt", "w") as file:
    file.write("This is my first ML note.")

# Reading from a file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)