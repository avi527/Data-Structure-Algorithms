# Write a python program to convert a 2D matrix into a sparse matrix 

#matrix of order 4 * 5
matrix = [[0,0,3,0,4],[0,7,0,4,0],[0,0,0,5,0],[0,1,0,0,0]]
#initialize size as 0
size = 0
#compute the number of nonzero elements in given matrix
for i in range(4):
	for j in range(5):
		if (matrix[i][j] != 0):
			size += 1
#number of row in sparseMatrix(size) should
#be equal to number of nonzero element in matrix
rows, cols = (size,3)
sparseMatrix = [[0 for i in range(cols)] for j in range(rows)]
k = 0
for i in range(4):
	for j in range(5):
		if (matrix[i][j] != 0):
			sparseMatrix[k][0] = i
			sparseMatrix[k][1] = j
			sparseMatrix[k][2] = matrix[i][j]
			k += 1
for i in sparseMatrix:
	print(i)