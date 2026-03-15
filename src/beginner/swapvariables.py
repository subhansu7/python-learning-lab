a=20
b=10
a=b
b=a
print(f"Value of a: {a}")  # Output: 10
print(f"Value of b: {b}")  # Output: 10
# In the above code, both a and b end up with the value 10 because we assigned a to b before assigning b to a.
# To swap the values of a and b correctly, we can use a temporary variable:
a=20
b=10
temp1=a
a=b
b=temp1
print(f"Value of a: {a}")  # Output: 10
print(f"Value of b: {b}")  # Output: 20
# Alternatively, we can swap the values without using a temporary variable:
# In Python, we can swap variables in a single line using tuple unpacking:
#Rotational Swapping, Pythonic swap
a=50
b=60
a, b = b, a
print(f"Value of a: {a}")  # Output: 60
print(f"Value of b: {b}")  # Output: 50

#Classsic swap , arithmetic swap without using a temporary variable
a=100
b=200
a = a+b  # a now holds the sum of a and b
b = a-b  # b now holds the original value of a
a = a-b  # a now holds the original value of b
print(f"Value of a: {a}")  # Output: 200
print(f"Value of b: {b}")  # Output: 100

#Swapping with XOR operator, a bitwise operator that can be used to swap values without a temporary variable:
a=300
b=400
a = a ^ b  # a now holds the result of a XOR b
b = a ^ b  # b now holds the original value of a
a = a ^ b  # a now holds the original value of b
print(f"Value of a: {a}")  # Output: 400
print(f"Value of b: {b}")  # Output: 300

