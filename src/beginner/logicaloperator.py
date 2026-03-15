#Generate codes for logical operator
a = True
b = False
print(f"Logical AND (a and b): {a and b}")  # Output: False
print(f"Logical OR (a or b): {a or b}")    # Output: True
print(f"Logical NOT (not a): {not a}")     # Output: False  
print(f"Logical NOT (not b): {not b}")     # Output: True

#Take 2 numbers instead of True and False
x = 5
y = 10
print(f"Logical AND (x > 0 and y > 0): {x > 0 and y > 0}")  # Output: True
print(f"Logical OR (x > 0 or y < 0): {x > 0 or y < 0}")    # Output: True
print(f"Logical NOT (not (x > 0)): {not (x > 0)}")     # Output: False

# Output: 10, because in Python, the 'and' operator returns the last evaluated value if all are true, 
# otherwise it returns the first evaluated value that is false. 
# In this case, both x and y are true (non-zero), so it returns the last evaluated value, which is y (10).
print (x and y) 
# Output: 5, because the 'or' operator returns the first evaluated value if it is true,
# otherwise it returns the last evaluated value
# In this case, x is true (non-zero), so it returns x (5) without evaluating y. 
print (x or y)

print (False or True)  # Output: True
print (False or True)  # Output: True
print (False and True)  # Output: False
print (True and False)  # Output: False
print (True and True)   # Output: True
print (False and False) # Output: False

