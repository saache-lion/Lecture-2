import numpy as np
points = np.random.randint(100, size=(3,2)) #creates a 2D array with random integers
central_point = np.array([50, 50])  #example central point


#numpy sum:
arr =[ [1, 2],
       [3, 4],
       [5, 6]
    ]
np_sum_1 = np.sum(arr, axis=0)  #axis=0 sums along the columns        
np_sum_2 = np.sum(arr, axis=1)  #axis=1 sums along the rows
np_sum_3 = np.sum(arr)  #sums all elements in the array


def euclidean_distance(points, central_point):
    distances = np.sqrt(np.sum((points - central_point) ** 2, axis=1))
    return distances

print("Points:", points)
print("Central Point:", central_point)
print("Distances:", euclidean_distance(points, central_point))

#checking which value is closest to the central point
distances = euclidean_distance(points, central_point)
closest_index = np.argmin(distances)  #index of the closest point
closest_point = points[closest_index]
print("Closest Point:", closest_point)
print("Distance to Closest Point:", distances[closest_index])

#arr[start:end:increment, start:end:increment] first one for columns, second one for rows
matrix = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [11, 22, 1, 2]])

print(matrix[2:, :3]) #Slicing - creates a view

print(matrix[[1,2],[2,2]]) #Fancy Indexing - creates a copy

#np.ix_ is used to create an open mesh from multiple sequences.
#It is useful for indexing multidimensional arrays.
#combo of indexing and slicing
rows = [0, 2]
cols = [1, 3]
print(matrix[np.ix_(rows, cols)])  #selects rows 0 and 2, and columns 1 and 3

#ex
grades = np.array([[85, 90, 78,88],
                  [92, 88, 95, 82],
                  [80, 85, 88, 91]])

student = [1,2]
subject = [1,3]
grades[np.ix_(student, subject)] = [[1,2],[45,90]] #selects students 1 and 2, and subjects 1 and 4
print("Updated Grades:\n", grades)