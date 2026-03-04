#Set operations in Python   
# Set is a collection which is unordered, unchangeable*, and unindexed.
# Sets are written with curly brackets.
# Create a set
myset = {"apple", "banana", "cherry"}
print(myset)
# Add an element to a set
myset.add("orange")
print(myset)

# Remove an element from a set
myset.remove("banana")
print(myset)

# Union of two sets
set1 = {"a", "b", "c"}  
set2 = {"c", "d", "e"}
union_set = set1.union(set2)
print(union_set)

# Symmetric difference of two sets (elements in either set but not both)
set3 = {"a", "b", "c"}
set4 = {"c", "d", "e"}
sym_diff = set3.symmetric_difference(set4)
print(sym_diff)  # {'a', 'b', 'd', 'e'}

# Note: the equivalent operator is ^ (e.g. set3 ^ set4)
# Intersection of two sets
intersection_set = set1.intersection(set2)  
print(intersection_set)

# Difference of two sets
difference_set1 = set1.difference(set2)
print(difference_set1)
difference_set2 = set2.difference(set1)
print(difference_set2) 

# Symmetric difference of two sets
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)

sym_diff_set2 = set2.symmetric_difference(set1)
print(sym_diff_set2)

# Check if a set is a subset of another set
set5 = {"a", "b"}
print(set5.issubset(set1))  # True
print(set1.issubset(set5))  # False
# Check if a set is a superset of another set
print(set1.issuperset(set5))  # True
print(set5.issuperset(set1))  # False


# Check if two sets are disjoint (no common elements)
set6 = {"x", "y", "z"}
print(set1.isdisjoint(set6))  # True
print(set1.isdisjoint(set2))  # False

# Clear a set
set1.clear()
print(set1)  # set()



