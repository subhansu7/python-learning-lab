list1 = [10, 20, 30, 40, 50]

#Python iterates over elements (values) of the list. i holds each item itself
for i in list1:
    print(i)

#Python iterates over the list and gives us both the index and the value of each item. 
# i holds a tuple of (index, value)
for i in enumerate(list1):
    print(i)

#unpacking the tuple into index and value
for index, value in enumerate(list1):
    print(f"Index: {index}, Value: {value}")
    print(f"Value mutiplied by 100: {value * 100}")
