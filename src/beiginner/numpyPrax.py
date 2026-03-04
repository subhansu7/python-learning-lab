import numpy as np
#print (np.__version__)
import sys
#print (sys.version)

my_list = [1,2,3,4,5]
print (my_list)
print (type(my_list))

# Converting list to array
my_array = np.array(my_list)
print (my_array)
print (type(my_array))

#Create 15 numbers
my_array2 = np.arange(15)
print (my_array2)

# start, stop, step
nparr2 = np.arange(0, 10, 2) 
print (nparr2)

#hyperparameters tuning
zeroarr = np.zeros(5)
print (zeroarr)

#print integer zeoros
zeroarr_int = np.zeros(5, dtype=int)
print(zeroarr_int)

onearr = np.ones(10, dtype=int)
print (onearr)

#print 2D array of zeros
zeroarr_2d = np.zeros((3,4), dtype=int)
print (zeroarr_2d)

#print multidimension array using tuple
n1 = (6,8)
print (type(n1))
multiarr = np.zeros(n1, dtype=int)
print (multiarr)

#Generate random numbers
#package.module.function
randarr = np.random.rand(5)
print (randarr)

#Generate 2D array of random numbers
randarr2 = np.random.rand(3,4)
print (randarr2)

#Generate random integers --low,high,size
randintarr = np.random.randint(5,10,2)
print (randintarr)

#Create 2d array of eye matrix
eyearr = np.eye(4,dtype=int)
print (eyearr)
