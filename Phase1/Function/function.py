# Built-in Functions
print("Hello")        # built-in function to display output
len([1, 2, 3])         # built-in function to get length → 3
type(10)               # built-in function to check type → <class 'int'>
max(4, 9, 2)           # built-in function → 9
sum([1, 2, 3])         # built-in function → 6


# User-Defined Functions

def myfunction(x):
    return x + 1
print(myfunction(5))


# Functions with Default Arguments

def greetme(name="ashwini"):
    return f"hello, {name}!"
print(greetme())
print(greetme("reyansh"))


# ## Functions with Variable Number of Arguments (*args, **kwargs) ####


# *args — accepts any number of positional arguments (as a tuple)

def number(*num):
    return sum(num)
print(number(1,2,3,4,5))

# **kwargs — accepts any number of named/keyword arguments (as a dictionary)

def print_profiles(**details):
    for key , value in details.items():
        print(f"{key}: {value}")
print_profiles(name="Ashwini",age=19, city="Delhi")