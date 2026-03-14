#
my_list=[10,20,30,40,50 ]
print(my_list)
print(my_list[0])

#length of list
print(len(my_list))

#append() method is used to add an element to the end of the list.
my_list.append(60)
print(my_list)

#copy() method is used to create a shallow copy of the list.
my_list_copy = my_list.copy()
print(my_list_copy)

#why copy() method is used to create a shallow copy of the list?
#The copy() method is used to create a shallow copy of the list because it creates a
my_list.append(70)
print ("Post appending to original list")
print(my_list)
print(my_list_copy)

print ("Post appending to copy list")
my_list_copy.append(80)
print(my_list)
print(my_list_copy)

#Below example demonstrate that copy() method creates a shallow copy of the list, which means that it creates a new list object but does not create copies of the objects contained within the original list.
#Instead, it references the same objects in memory. Therefore, if you modify a mutable object (like a list) within the copied list, it will affect the original list as well.
a = [1, 2, [3, 4]]
b = a.copy()
# False (different lists)
print(a is b)        
# True  By coincidence
print(a[1] is b[1])
 # True  (same inner list). In memopry, both a and b reference the same inner list [3, 4].  
print(a[2] is b[2]) 

b[2].append(5)
print(a)  # Output: [1, 2, [3, 4, 5]]
print(b)  # Output: [1, 2, [3, 4, 5]]

#Deep copy is a process of creating a new list object and recursively copying all the objects contained within the original list. This means that if you modify a mutable object (like a list) within the copied list, it will not affect the original list.
#Updating inner list in b will not affect a because they are different inner lists in memory.
import copy
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)   
print(a is b)        # False (different lists)
print(a[1] is b[1])  # False (different inner lists)
print(a[2] is b[2])  # False (different inner lists)
b[2].append(5)
print(a)  # Output: [1, 2, [3, 4]]
print(b)  # Output: [1, 2, [3, 4, 5]]

#Remove() method is used to remove the first occurrence of a specified value from the list.
my_list.remove(30)
print(my_list)

my_list.append(30)
my_list.append(30)
print(my_list)
my_list.remove(30)
print(my_list)

#pop() method is used to remove and return an element from the list based on the specified index. If no index is provided, it removes and returns the last element of the list.
print(my_list.pop())  # Removes and returns the last element (30)
print(my_list)
print(my_list.pop(0))  # Removes and returns the element at index 0 (10)
print(my_list)

#insert() method is used to insert an element at a specified index in the list.
my_list.insert(0, 10)  # Inserts 10 at index 0  
print(my_list)
my_list.insert(2, 25)  # Inserts 25 at index 2  
print(my_list)
#insert method behavior if index is greater than the length of the list
my_list.insert(10, 100)  # Inserts 100 at index 10 (which is beyond the current length of the list)
print(my_list)  # Output: [10, 20, 25, 40, 50, 60, 70, 100]

#extend() method is used to extend the list by appending all the items from another iterable (e.g., another list).
my_list.extend([80, 90, 100])
print(my_list)

#clear() method is used to remove all elements from the list, resulting in an empty list.
my_list.clear()
print(my_list)  # Output: []

#delete() method is used to delete an element from the list based on the specified index. It can also be used to delete a slice of the list or the entire list.
my_list = [10, 20, 30, 40, 50]
del my_list[0]  # Deletes the element at index 0 (10)
print(my_list)  # Output: [20, 30, 40, 50]
del my_list[1:3]  # Deletes the elements from index 1 to 2 (30 and 40)
print(my_list)  # Output: [20, 50]
del my_list  # Deletes the entire list
# print(my_list)  # This will raise an error because my_list has been deleted
# NameError: name 'my_list' is not defined 
#print(my_list)

my_list = [10, 20, 30, 40, 50]
my_list.clear()
print(my_list)  # Output: []
del my_list
#print(my_list)  # This will raise an error because my_list has been deleted
# NameError: name 'my_list' is not defined

#index() method is used to return the index of the first occurrence of a specified value in the list. If the value is not found, it raises a ValueError.
my_list = [10, 20, 30, 40, 50]
print(my_list.index(30))  # Output: 2
#print(my_list.index(60))  # This will raise a ValueError because 60 is not in the list
#ValueError: 60 is not in list

#count() method is used to return the number of occurrences of a specified value in the list.
my_list = [10, 20, 30, 40, 50, 30, 30]
print(my_list.count(30))  # Output: 3  

#sort() method is used to sort the elements of the list in ascending order by default. It can also be used to sort the elements in descending order by passing the reverse=True argument.
my_list = [30, 10, 50, 20, 40]  
my_list.sort()  # Sorts the list in ascending order
print(my_list)  # Output: [10, 20, 30, 40, 50]
my_list.sort(reverse=True)  # Sorts the list in descending order    
print(my_list)  # Output: [50, 40, 30, 20, 10]

#reverse() method is used to reverse the order of the elements in the list.
my_list.reverse()
print(my_list)  # Output: [10, 20, 30, 40, 50]  

#slicing is a powerful technique in Python that allows you to extract a portion of a list (or any sequence) by specifying a range of indices. The syntax for slicing is as follows:
# list[start:stop:step]
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])  # Output: [20, 30, 40]
print(my_list[:3])   # Output: [10, 20, 30]
print(my_list[2:])   # Output: [30, 40, 50]
print(my_list[::2])  # Output: [10, 30, 50] (step of 2)


print(my_list[-4])
print(my_list[-2])
#In case of negative step, start index should be gerater than stop index (post converytion to positive index) otherwise it will return empty list.  
#In case of positive step, start index should be less than stop index (post converytion to positive index) otherwise it will return empty list.
#print(my_list[-4:-2:-1])
print(my_list[-2:-4:-1])
print(my_list[4:2:-1])
#For below case, step is negative, default start  index is length of list -1, 
# Default stop index is -1, so it not ignore last element in reverse order.
print(my_list[::-1]) # Output: [50, 40, 30, 20, 10] (reverse order) 
