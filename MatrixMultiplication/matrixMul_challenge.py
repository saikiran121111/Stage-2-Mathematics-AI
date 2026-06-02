import numpy as np
# Level 1 — Absolute Basics:
#
# Create a 2x2 matrix: [[1, 2], [3, 4]]
#
# Create a vector: [10, 20]
#
# Multiply the matrix by the vector using the @ operator and print the result.
#
# Expected Output: [50 110]

mat = np.array([[1,2],[3,4]])

vec = np.array([10,20])

total = mat @ vec

print(total)

# Level 2 — Real-life Application (Multi-Employee Payroll):
#
# Let's look at Alice, Bob, and Charlie from your dataset.
#
# Create a matrix where each row represents [Base Salary, Monthly Bonus] for them: [[50000, 2000], [60000, 0], [55000, 4000]]
#
# The tax department applies a multiplier vector of [0.8, 0.9] (meaning 80% of base salary is kept after tax, and 90% of the bonus is kept).
#
# Multiply the employee matrix by the tax vector using @ to find their final take-home income.
#
# Expected Output: [41800. 48000. 47600.]

mat = np.array([[50000, 2000], [60000, 0], [55000, 4000]])

vec = np.array([0.8,0.9])

print( mat @ vec)

# Level 3 — Interview Trap (The Shape Mismatch):
#
# Create a matrix of shape (3, 2): [[1, 2], [3, 4], [5, 6]]
#
# Create a vector with 3 elements: [10, 20, 30]
#
# Try to multiply matrix @ vector. It will throw an error because the row width (2) doesn't match the vector height (3).
#
# Wrap it in a try...except ValueError: block and print: "Interview Trap: Shape mismatch!"
#
# Expected Output: Interview Trap: Shape mismatch!

mat = np.array([[1, 2], [3, 4], [5, 6]])
vec = np.array([10,20,30])

try:
    print(mat @ vec)
except ValueError:
    print('Interview Trap: Shape mismatch!')


# Level 4 — Mastery (Under the Hood):
#
# Let's prove you know how the computer handles this mathematically.
#
# Create a matrix as a standard Python list of lists: matrix = [[2, 3], [4, 5]]
#
# Create a vector as a standard Python list: vector = [10, 2]
#
# Without using NumPy, use standard Python loops to calculate the matrix-vector multiplication.
#
# Hint: Create an empty list result = []. Loop through each row of your matrix, calculate the manual dot product between that row and the vector, and append the total to your result list.
#
# Print your final result list.
#
# Expected Output: [26, 50]

mat = [[2,3],[4,5]]

vec = [10,2]
print('#######################')
result = []
for row in mat:
    totalval = sum(i*j for i,j in zip(row,vec))
    result.append(totalval)

print(result)