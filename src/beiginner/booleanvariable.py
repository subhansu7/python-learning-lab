a = True
b = False
print (a+b)
print (a)

# bool() function is used to convert a value to a boolean value (True or False) based on the following rules:
# - The following values are considered False: None, False, 0, 0.0, 0.0, 0j, empty sequences (e.g., '', (), []), and empty mappings (e.g., {}).
# - All other values are considered True.
print (bool(0) == False)
print (bool(1) == True)
print (bool(-1) == True)
print (bool("") == False)
print (bool(" ") == True)
print (bool() == False)