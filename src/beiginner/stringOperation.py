#String
print ("###String Operations###")
s = "Hello World"
print ("Original String =>" +  s)
print (type(s))
print ("Length of string"+ " " +str(len(s)))
print (s[0], s[10])
#Start, stop, step
#start → included, stop → excluded, Default step = +1
#Python always slices left → right when step is positive
print (s[0:5])
print (s[1:6:2])

#backward slicing
print (s[-1])
print (s[-5:-1])
print (s[-1:-5:-2])
print (s[-5:-1:-2])

#slicing and till end of string"
print("###slicing and till end of string###")
print (s[6:])
print (s[-3:])

#slicing from beginning of string
print("###slicing from beginning of string###")
print (s[:5])
print (s[:-6])

#String Unpacking
print ("###String Unpacking###")
a,b,c,d,e,f,g,h,i,j,k = s
print (a)
print (b)

#Counting the number of times a character appears in a string,
#count() method returns the number of occurrences of a substring in the given string. 

print ("###Counting the number of times a character appears in a string###")
print (s.count('o'))
# We can mention start and end index to specify the range in which we want to count the occurrences of the substring. The default value of start is 0 and end is the length of the string.
print (s.count('o', 5, 11))

#Formatting Strings
print ("###Formatting Strings###")
name = "Alice"
age = 30
#Using f-strings (available in Python 3.6 and later)
print (f"My name is {name} and I am {age} years old.")
#Using str.format() method
print ("My name is {} and I am {} years old.".format(name, age))

#Check all characters in the string are alphanumeric
print ("###Check all characters in the string are alphanumeric###") 
s1 = "Hello123"
s2 = "Hello 123"    
print (s1.isalnum())  # True
print (s2.isalnum())  # False (contains a space)

#Check all characters in the string are alphabetic
print ("###Check all characters in the string are alphabetic###")   
s3 = "Hello"
s4 = "Hello123"
print (s3.isalpha())  # True
print (s4.isalpha())  # False (contains digits)

#Check all characters in the string are digits
print ("###Check all characters in the string are digits###")   
s5 = "12345"
s6 = "12345a"   
print (s5.isdigit())  # True
print (s6.isdigit())  # False (contains a letter)

#Check all characters in the string are whitespace
print ("###Check all characters in the string are whitespace###")
s7 = "   "
s8 = " Hello "
print (s7.isspace())  # True
print (s8.isspace())  # False (contains non-whitespace characters)

#Check if the string is in title case
print ("###Check if the string is in title case###")
s9 = "Hello World"
s10 = "hello world"
print (s9.istitle())  # True
print (s10.istitle())  # False (not in title case)

#Check if the string is in uppercase
print ("###Check if the string is in uppercase###") 
s11 = "HELLO"
s12 = "Hello"
s13 = "hello"
print (s11.isupper())  # True
print (s12.isupper())  # False (not in uppercase)
print (s13.isupper())  # False (not in uppercase)   
print (s13.islower())  # True (all characters are lowercase )

#case conversion
print ("###case conversion###")
s14 = "Hello World"
#Convert the string to uppercase
upper_s14 = s14.upper()
print (upper_s14)  # Output: "HELLO WORLD"
#Convert the string to lowercase
lower_s14 = s14.lower()
print (lower_s14)  # Output: "hello world"

#Joining and splitting strings
print ("###Joining and splitting strings###")   
words = ["Hello", "World", "Python"]
#Joining a list of strings into a single string with a space as a separator
sentence = " ".join(words)
print (sentence)  # Output: "Hello World Python"

#Splitting a string into a list of substrings based on a separator
s14 = "Hello,World,Python"
#Splitting the string into a list of substrings using comma as a separator
substrings = s14.split(",")
print (substrings)  # Output: ['Hello', 'World', 'Python']

#Stripping whitespace from strings
print ("###Stripping whitespace from strings###")
s15 = "   Hello World   "
#Removing leading and trailing whitespace from the string
stripped_string = s15.strip()
print (stripped_string)  # Output: "Hello World"    
#Removing only leading whitespace
lstripped_string = s15.lstrip()         
print (lstripped_string)  # Output: "Hello World   "
#Removing only trailing whitespace
rstripped_string = s15.rstrip()
print (rstripped_string)  # Output: "   Hello World"

#Strip a specific character from the string
s16 = "###Hello World###"
print ("###Strip characters from strings###")
#Removing leading and trailing '#' characters from the string
stripped_string2 = s16.strip("#")
print (stripped_string2)  # Output: "Hello World"

#Replaceing substrings in a string
print ("###Replaceing substrings in a string###")
s17 = "Hello World"
#Replacing "World" with "Python" in the string
replaced_string = s17.replace("World", "Python")
print (replaced_string)  # Output: "Hello Python"

#Finding the index of a substring in a string
print ("###Finding the index of a substring in a string###")
s18 = "Hello World"
#Finding the index of the first occurrence of "World" in the string
index = s18.find("World")
print (index)  # Output: 6
#Finding the index of a substring that does not exist in the string
index_not_found = s18.find("Python")
print (index_not_found)  # Output: -1 (substring not found)

