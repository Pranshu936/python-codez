# Function to take matrix input from the user
def input_matrix(rows, cols):
    matrix = []
    print(f"Enter {rows} rows and {cols} columns for the matrix:")
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("Invalid input. Please enter exactly", cols, "elements for each row.")
            return None
        matrix.append(row)
    return matrix

# Function to perform matrix multiplication
def matrix_multiplication(A, B):
    if len(A[0]) != len(B):
        print("Matrix multiplication not possible. Number of columns in first matrix should be equal to number of rows in second matrix.")
        return None

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            # Calculate element (i, j) of the result matrix
            element = 0
            for k in range(len(B)):
                element += A[i][k] * B[k][j]
            row.append(element)
        result.append(row)
    return result

# Main function
def main():
    # Input for dimensions of matrices
    rows_A, cols_A = map(int, input("Enter dimensions of Matrix A (rows columns): ").split())
    rows_B, cols_B = map(int, input("Enter dimensions of Matrix B (rows columns): ").split())

    # Input matrices A and B
    print("Input Matrix A:")
    A = input_matrix(rows_A, cols_A)
    if A is None:
        return
    print("Input Matrix B:")
    B = input_matrix(rows_B, cols_B)
    if B is None:
        return

    # Perform matrix multiplication
    result = matrix_multiplication(A, B)

    # Print the result
    if result:
        print("Result of Matrix Multiplication A*B:")
        for row in result:
            print(row)

if __name__ == "__main__":
    main()
