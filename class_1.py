#Scaler : Single Value Array

#Vector : Multi Value Array

#List
A = [1, 2, 3, 4, 5]
B = [6, 7, 8, 9, 10]

def add_vectors(a, b):
    result = []
    if len(a) != len(b):
        return "Vectors must be of the same length"
    else:
        for i in range(len(a)):
            result.append(a[i] + b[i])
    return result

print(add_vectors(A, B)) #does not matter what we call these variables, they can be anything
#Need to loop through the elements of the list and add them
#Quite inefficient

#Numpy Arrays
import numpy as np
u = np.array([2,3,4])
v = np.array([1,2,3])

print(u + v)  #element-wise addition
#Numpy Arrays inbilt functions are optimized for performance

#Broadcasting
A = np.array([[1, 2, 3],
               [4, 5, 6]]) #(2,3) shape
B = np.array([10, 20, 30]) #(1,3) shape

B1 = np.array([[10, 20, 30],
               [10, 20, 30]]) #(2,3) shape
#A+B = A+B1
print(A + B)  #B is broadcasted to match the shape of A
print(A + B1)  #B1 has the same shape as A, so no broadcasting needed

#npA = np.array([1], [2], [3])  #shape (3,1)

#npB = np.array([4, 5, 6,5], [5,8,9,10], [5,1,0,5] )  #shape (3,)

#print(npA + npB)  #Broadcasting will not work here, shapes are incompatible

#To create a 2D array with random integers
#We can use np.random.randint
a =  np.random.randint(100, size=(4,4))#3 rows, 4 columns
b = np.random.randint(100, size=(2,2)) 
print(a)
print(b)
#print(a+b)  #Broadcasting does not works here
#print(b+a) 

#Numpy Arrays are more efficient than lists for numerical operations
#They are optimized for performance and memory usage

#Numpy vs List Performance Comparisonp.random.randint(100, size=(4,4))n
#Let's compare the performance of numpy arrays and lists for addition

n=1_000_000_000  #1 million elements
u = np.arange(n)
v = np.arange(n)

import time as t
#Time the addition of numpy arrays and lists
start = t.time()
print(u + v) 
end = t.time()
print(f"Time taken for numpy addition:  {(end - start):.4f}")

#Now let's compare it with lists
start1 = t.time()
def add_vectors(a, b):
    result = []
    if len(a) != len(b):
        return "Vectors must be of the same length"
    else:
        for i in range(len(a)):
            result.append(a[i] + b[i])
    return result
end1 = t.time() 
print(f"Time taken for list addition: {(end1 - start1):.4f}")

#Numpy arrays are significantly faster than lists for numerical operations
#This is because numpy uses optimized C libraries under the hood

#vectorization
#Numpy allows us to perform operations on entire arrays without explicit loops
#ED formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
#Let's calculate the Euclidean distance between two points in 2D space using numpy  

#points = [[x1, y1], [x2, y2]...]
#central_point = [X,Y]
#distances = [d1,d2,d3..] ->output

points = np.random.randint(100, size=(2,1)) #creates a 2D array with random integers
central_point = np.array([50, 50])  #example central point

def euclidean_distance(points, central_point):
    distances = np.sqrt(np.sum((points - central_point) ** 2, axis=1))
    return distances

print("Points:", points)
print("Central Point:", central_point)
print("Distances:", euclidean_distance(points, central_point))