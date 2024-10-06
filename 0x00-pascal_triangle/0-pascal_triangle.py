#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)  # Start with a row of ones
        for j in range(1, i):  # Calculate the values in the middle
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

# Example usage:
print(pascal_triangle(5))
