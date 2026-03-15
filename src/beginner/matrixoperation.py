import numpy as np
#Generating a Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#why we are using numpy array instead of list of lists to represent a matrix?
#Numpy arrays are more efficient than lists of lists for representing matrices because they are implemented in
## If we try to use list.shape, it will raise an AttributeError because lists do not have a shape attribute.
matrix=np.array(matrix)
print(matrix)
print(matrix.shape)  
#To get the shape of a matrix, you can use the len() function to get the number of rows and columns.
rows = len(matrix)
cols = len(matrix[0]) if rows > 0 else 0
print(f"Shape of the matrix: ({rows}, {cols})")
