#!/usr/bin/python3
def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate each row of the triangle
    for i in range(1, n):
        # Start the row with a 1
        row = [1]
        # Calculate the values for the middle of the row
        for j in range(1, i):
            # Each value is the sum of the two values above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End the row with a 1
        row.append(1)
        # Add the row to the triangle
        triangle.append(row)

    return triangle

# Example usage:
print(pascal_triangle(5))
