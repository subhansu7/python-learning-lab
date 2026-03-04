#Dictionary examples with different operations

#Creating a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

#Accessing valuesprint(my_dict["name"])  # Output: Alice
print (my_dict["age"])  # Output: 30
print(my_dict.get("age"))  # Output: 30

#Adding a new key-value pair    
print ("Before adding new key-value pair:  ", my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
my_dict["country"] = "USA"
print ("After adding new key-value pair:  ", my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}
#Updating an existing key-value pair
my_dict["age"] = 31
print ("After updating age:  ", my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}

#Removing a key-value pair
del my_dict["city"]
print ("After removing city:  ", my_dict)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}

#Iterating through a dictionary
print ("Iterating through dictionary:  ")   
for key, value in my_dict.items():
    print(f"{key}: {value}")    

#Checking if a key exists
print ("Checking if 'name' key exists:  ", "name" in my_dict)  # Output: True
print ("Checking if 'city' key exists:  ", "city" in my_dict)  # Output: False

#Getting all keys and values
print ("All keys:  ", my_dict.keys())  # Output: dict_keys(['name', 'age', 'country'])
print ("All values:  ", my_dict.values())  # Output: dict_values(['Alice', 31, 'USA'])

#Clearing the dictionary
my_dict.clear()
print ("After clearing dictionary:  ", my_dict)  # Output: {}

#Creating a dictionary using dict() constructor
new_dict = dict(name="Bob", age=25, city="Los Angeles")
print ("New dictionary created using dict() constructor:  ", new_dict)  # Output: {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}

#Merging two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2) # Merges dict2 into dict1, overwriting existing keys of dict1 with values from dict2
print ("After merging dict1 and dict2:  ", dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

#Using dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
print ("Dictionary created using comprehension:  ", squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#Using setdefault() method
my_dict.setdefault("name", "Charlie")  # Does not change 'name' since it already exists
my_dict.setdefault("country", "USA")  # Does not change 'country' since it already exists
my_dict.setdefault("age", 35)  # Does not change 'age' since it already exists
print ("After using setdefault():  ", my_dict)  # Output: {'name': 'Charlie', 'country': 'USA', 'age': 35}  

#Using pop() method to remove a key-value pair and return the value
age = my_dict.pop("age", None)  # Removes 'age' and returns its value, or returns None if 'age' does not exist
print ("Popped age:  ", age)  # Output: 35
print ("After popping age:  ", my_dict)  # Output: {'name': 'Charlie', 'country': 'USA'}

#Using popitem() method to remove and return an arbitrary key-value pair
item = my_dict.popitem()  # Removes and returns an arbitrary key-value pair as a tuple
print ("Popped item:  ", item)  # Output: ('country', 'USA') or ('name', 'Charlie') depending on the order of items in the dictionary
print ("After popping an item:  ", my_dict)  # Output: {'name': 'Charlie'} or {} depending on the order of items in the dictionary

#Using fromkeys() method to create a new dictionary with specified keys and a default value
keys = ["name", "age", "city"]
default_value = "Unknown"
new_dict = dict.fromkeys(keys, default_value)   
print ("New dictionary created using fromkeys():  ", new_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

#Using copy() method to create a shallow copy of a dictionary
original_dict = {"name": "Alice", "age": 30}    
copied_dict = original_dict.copy()  # Creates a shallow copy of original_dict
print ("Original dictionary:  ", original_dict)  # Output: {'name': 'Alice', 'age': 30}
print ("Copied dictionary:  ", copied_dict)  # Output: {'name': 'Alice', 'age': 30}

#demonstarte duplicate keys in a dictionary are not allowed, the last value will overwrite the previous one
duplicate_key_dict = {"key1": "value1", "key2": "value2", "key1": "value3"}
print ("Dictionary with duplicate keys:  ", duplicate_key_dict)  # Output: {'key1': 'value3', 'key2': 'value2'} - 'key1' has the value 'value3' because it overwrote 'value1'       

dict1 = dict(key1='val1', key2='val2')
print(dict1)
