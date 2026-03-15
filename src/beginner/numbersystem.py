# Number system example in Python
# This program demonstrates the conversion of numbers between different number systems
a=20
print(f"Decimal Number: {a}")
print(f"Binary Representation: {bin(a)}")  # Output: '0b10100'
print(f"Octal Representation: {oct(a)}")   # Output: '0o24'
print(f"Hexadecimal Representation: {hex(a)}")  # Output: '0x14'

b = 0b10100  # Binary representation of 20
print(f"Decimal from Binary: {b}")  # Output: 20
#base=2 is used to specify that the string is in binary format
print(f"Integer from Binary: {int('1111', 2)}")  # Output: 15
print(f"Integer from Octal: {int('1111', 8)}")  # Output: 589
print(f"Integer from Hexadecimal: {int('1111', 16)}")  # Output: 4369

def decimal_to_binary(n):
    """Convert a decimal number to binary."""
    #print ("Hello, welcome to the number system converter!")
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary
binary_number = decimal_to_binary(10)  # Output: '1010'
print(f"Binary Number: {binary_number}")