#Typecasting
print ("Typecasting")
print (int(3.5))
print (int(3.6))
print (int(3.9))
print (float(3))
print (float(True))
print (int(False))
print (str(3))
#TypeError: float() argument must be a string or a real number, not 'complex'
#print (float(2+3j))
#ValueError: could not convert string to float: 'hello'
#print(float("hello"))
#Python’s float() does not expect only numeric types.
#it expects something that can be converted to a number.
print(float("3"))

print (complex(3))
print (complex(3,4))
#Commas separate values — they don’t create default values.
#print (complex(,4))
#The comma does not mean “missing value”
#It’s just a trailing comma, which Python allows
#imag is optional. If imag is not provided → Python uses its default value = 0
print (complex(4,))

#complex(real) → imag defaults to 0
#Coversion rule = bool → int → float → complex
print (complex(True))
print (complex(False))