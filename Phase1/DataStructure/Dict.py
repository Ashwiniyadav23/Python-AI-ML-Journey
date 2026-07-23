# Dictionary (dict) — labeled data (like a mini-database)

students = [
    {"name": "Ashwini", "age": 19, "grade": 89}
]

print(students) # Print the entire list

print(students[0])  # Access the first dictionary (student) from the list

print(students[0]["age"])  # Access a specific value using its key

students[0]["age"] = 20  # Update the value of the "age" key
print(students)  # Print the updated list

del students[0]["grade"]  # Delete the "grade" key from the first student's dictionary
print(students)   # Print the final list after deletion
