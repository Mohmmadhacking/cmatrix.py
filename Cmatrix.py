import random

# Define the characters to be used in the matrix
characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '#', '$', '%', '&', '*', '+', '-', '/', '=', '?']

# Define the size of the matrix
matrix_size = 5

# Create an empty matrix
matrix = [[' ' for x in range(matrix_size)] for y in range(matrix_size)]

# Fill the matrix with random characters
for i in range(matrix_size):
    for j in range(matrix_size):
        matrix[i][j] = random.choice(characters)

# Print the matrix
for i in range(matrix_size):
    for j in range(matrix_size):
        print(matrix[i][j], end=' ')
    print()
