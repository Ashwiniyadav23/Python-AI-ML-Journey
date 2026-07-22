# arithmetic operators

a = 10
b = 3

print(a + b)   # 13   → addition
print(a - b)   # 7    → subtraction
print(a * b)   # 30   → multiplication
print(a / b)   # 3.333333...  → division (always gives a decimal in Python)
print(a // b)  # 3    → floor division (division, but rounds DOWN to a whole number)
print(a % b)   # 1    → modulus (the REMAINDER left after dividing)
print(a ** b)  # 1000 → exponent (10 to the power of 3)


# Compare >, <, ==

x = 10
y = 20

print(x > y)    # False  → is 10 greater than 20? No
print(x < y)    # True   → is 10 less than 20? Yes
print(x == y)   # False  → is 10 equal to 20? No

# Compare >=, <=, !=

print(x >= y)   # False  → is 10 greater than or equal to 20? No
print(x <= y)   # True   → is 10 less than or equal to 20? Yes
print(x != y)   # True   → is 10 NOT equal to 20? Yes


# Combine: and, or, not

age = 25
has_id = True

can_enter_club = age >= 18 and has_id
print(can_enter_club)   # True  (both conditions are True)

has_student_id = False
has_teacher_id = True

gets_discount = has_student_id or has_teacher_id
print(gets_discount)   # True  (teacher ID alone is enough)

is_not_member = not has_id
print(is_not_member)   # False  (has_id is True, so not has_id is False)