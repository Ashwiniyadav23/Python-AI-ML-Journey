# String Manipulation & f-strings

name = "Ashwini"
age = 21

message = f"Hello, {name}! You are {age} years old."
print(message)



# 1. Creating Strings
s1 = "Hello"
s2 = 'World'
s3 = """This is a
multi-line string"""

print(s1)   # Hello
print(s2)   # World
print(s3)



# 2. Accessing Characters

word = "Python"
print(word[0])    # P   → first character
print(word[3])    # h   → 4th character

# 3. Joining Strings

first = "Hello"
second = "World"

combined = first + " " + second
print(combined)   # Hello World

words = ["I", "love", "Python"]
sentence = " ".join(words)
print(sentence)   # I love Python


# 4. Changing Case


text = "Hello World"

print(text.upper())     # HELLO WORLD
print(text.lower())     # hello world
print(text.title())     # Hello World  (capitalizes each word)
print(text.capitalize())# Hello world  (capitalizes only the first letter)

# 5. Finding Text


sentence = "I love learning Python"

print(sentence.find("learning"))    # 7   → starting index where "learning" begins
print("Python" in sentence)         # True  → checks if the text exists at all
print(sentence.count("o"))          # 3   → counts how many times "o" appears

# 6. Replacing Text

sentence = "I love Java"

updated = sentence.replace("Java", "Python")
print(updated)   # I love Python


# 7. Formatting Strings
name = "Ashwini"
age = 19

message = f"My name is {name} and I am {age} years old."
print(message)   # My name is Ashwini and I am 19 years old.


