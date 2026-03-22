#Function to demonstrate pass by value and pass by reference
def modify_list(lst):
    lst = [100, 200]   # lst points to new object

a = [1, 2, 3]
print(a)
modify_list(a)
print(a)

def modify_int(x):
    return x+10
b= 20
modify_int(b)
print (b)