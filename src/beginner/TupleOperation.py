#define single empty tuple
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple)) #<class 'tuple'>
#tuple with multiple values
my_tuple = (1, 2, 3, 4, 5)
print (len(my_tuple)) #5

#tuple with different data types
mixed_tuple = (1, "Hello", 3.14, [1, 2, 3], (4, 5))
print(mixed_tuple)

#modify a tuple 
#mixed_tuple[1] = "World" #TypeError: 'tuple' object does not support item assignment
#print(mixed_tuple)

#how to modify a tuple? we can convert it to a list, modify the list, and then convert it back to a tuple
temp_list = list(mixed_tuple) #convert tuple to list
temp_list[1] = "World" #modify the list
modified_tuple = tuple(temp_list) #convert back to tuple
print(modified_tuple) #(1, 'World', 3.14, [1, 2, 3], (4, 5))

#modifying a tuple is not allowed, but we can create a new tuple by concatenating two tuples    
tuple1 = (1, 2, 3)  
tuple2 = (4, 5, 6)
new_tuple = tuple1 + tuple2
print(new_tuple) #(1, 2, 3, 4, 5, 6)

#delete a tuple
#del modified_tuple[0] #TypeError: 'tuple' object doesn't support item deletion
#print (modified_tuple)
del modified_tuple #deletes the entire tuple allowed. But deleting single item is not allowed.
#print (modified_tuple) #NameError: name 'modified_tuple' is not defined

#iterate over a tuple
for item in new_tuple:
    print(item)

if (5 in new_tuple ):
    print("5 is in the tuple")
else:
    print("5 is not in the tuple")

#sort a tuple. sorted function when applied on any data structure returns a sorted list. So we can use sorted() to sort a tuple, but it will return a list, not a tuple. To get a sorted tuple, we can convert the sorted list back to a tuple.
my_tuple = (5, 2, 9, 1, 3)  
sorted_tuple = sorted(my_tuple) 
print (sorted_tuple) #[1, 2, 3, 5, 9] #sorted() returns a list, not a tuple
#to get a sorted tuple, we can convert the sorted list back to a tuple
sorted_tuple = tuple(sorted(my_tuple))  
print (sorted_tuple) #(1, 2, 3, 5, 9)

#Sorted does not do an in-place (inline) update

#counting occurrences of an element in a tuple
my_tuple = (1, 2, 3, 2, 4, 2, 5)
count_2 = my_tuple.count(2) 
print(f"Number of occurrences of 2: {count_2}") #3

#finding the index of an element in a tuple
index_3 = my_tuple.index(3) 
print(f"Index of 3: {index_3}") #2

##
#




