"""
Hacker Rank problem: Max Sum of Upper Left Quadrant

Take in a 2n x 2n matrix and find the maximum sum of the nxn upper left quadrant by only reversing columns and rows
"""


def maximize_upper_left_quadrant(matrix):
    n = len(matrix) // 2  # Determine the size of n

    # Function to compute the sum of the upper-left n x n quadrant
    def quadrant_sum(mat):
        return sum(mat[i][j] for i in range(n) for j in range(n))

    max_sum = float('-inf')  # Initialize maximum sum
    size = len(matrix)  # Full size of the matrix

    # Iterate through all row and column reversal combinations
    for row_flip in [False, True]:
        for col_flip in [False, True]:
            # Make a copy of the matrix for transformation
            temp_matrix = [row[:] for row in matrix]

            # Reverse rows if needed
            if row_flip:
                temp_matrix = temp_matrix[::-1]

            # Reverse columns if needed
            if col_flip:
                temp_matrix = [row[::-1] for row in temp_matrix]

            # Calculate the sum of the upper-left quadrant
            current_sum = quadrant_sum(temp_matrix)

            # Update maximum sum
            max_sum = max(max_sum, current_sum)

    return max_sum

# Example matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Call the function
result = maximize_upper_left_quadrant(matrix)
print("Maximum sum of upper-left quadrant:", result)
