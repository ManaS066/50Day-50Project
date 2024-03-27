def read_matrix(n):
    # Read the matrix
    matrix = []
    for _ in range(n):
        row = input().strip().split(',')
        row = list(map(int, row))
        matrix.append(row)
    return matrix


def multiply_matrix(matrix, inc):
    # Multiply each element of the matrix by the increment value
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= inc
    return matrix


def print_matrix(matrix):
    # Print the matrix
    for row in matrix:
        print(','.join(map(str, row)))


# Read the size of the square matrix
n = int(input())

# Read the matrix
A = read_matrix(n)
A = read_matrix(n)
# Read the increment value
inc = int(input())

# Multiply the matrix by the increment value
A_f = multiply_matrix(A, inc)

# Print the resulting matrix
print_matrix(A_f)
