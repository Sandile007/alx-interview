#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)  # Start with a row filled with 1s
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]  # Sum the two values above
        triangle.append(row)
    
    return triangle

# Test cases
print(pascal_triangle(1))  # Output: [[1]]
print(pascal_triangle(5))  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print(pascal_triangle(10)) # Output: The first 10 rows of Pascal's triangle
print(pascal_triangle(0))  # Output: []
print(pascal_triangle(100)) # Output: The first 100 rows of Pascal's triangle
