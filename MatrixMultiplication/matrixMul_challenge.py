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

print('#####################################################################################')
# Matrix X Matrix Multiplication

# Level 1 — Absolute Basics:
#
# Create Matrix A: [[1, 2], [3, 4]]
#
# Create Matrix B: [[5, 6], [7, 8]]
#
# Multiply them using @ and print the result.
#
# Expected Output:
#
# [[19 22]
#  [43 50]]

matA = np.array([[1,2],[3,4]])
matB = np.array([[5,6],[7,8]])

print(matA @ matB)
print('########')

# Level 2 — Real-life Application (Performance vs Cost Plans):
#
# Create a matrix of 2 employees and their [Tech Score, Comm Score]: [[80, 90], [70, 60]]
#
# Create a matrix of 2 company evaluation strategies: [[0.7, 0.5], [0.3, 0.5]] (Strategy 1 heavily favors tech, Strategy 2 evaluates both metrics equally).
#
# Multiply the employee matrix by the strategy matrix using @ to find the final scores under both strategies.
#
# Expected Output:
#
# [[83. 85.]
#  [67. 65.]]

matA = np.array([[80,90],[70,60]])
matB = np.array([[0.7,0.5],[0.3,0.5]])

print(matA @ matB)

# Level 3 — Interview Trap (The Dimension Mismatch):
#
# Create Matrix X of shape (3, 2): [[1, 2], [3, 4], [5, 6]]
#
# Create Matrix Y of shape (3, 2): [[7, 8], [9, 10], [11, 12]]
#
# Try to multiply X @ Y. (It will crash because the inner dimensions 2 and 3 don't match!)
#
# Wrap your execution in a try...except ValueError: block and print: "Interview Trap: Inner dimensions must match for matrices!"
#
# Expected Output: Interview Trap: Inner dimensions must match for matrices!


matX = np.array([[1,2],[3,4],[5,6]])
matY = np.array([[7,8],[9,10],[11,12]])

try:
    print(matX @ matY)
except ValueError:
    print('Interview Trap: Inner dimensions must match for matrices!')


# Level 4 — Mastery (The Triple Nested Loop - Under the Hood):
# Interviewers want to see if you actually know what the computer is doing during matrix multiplication. Let's do it without NumPy.
#
# Create Matrix C as a standard list: [[1, 2], [3, 4]]
#
# Create Matrix D as a standard list: [[2, 0], [1, 2]]
#
# Without using NumPy, write a pure Python script using nested loops to multiply Matrix C by Matrix D.
#
# Hint: You will need three nested loops (for i..., for j..., for k...) or standard list comprehensions to build the new rows and columns.
#
# Print your final list of lists.
#
# Expected Output: [[4, 4], [10, 8]]
#
# Take your time. Paste your code and type "done" when you are ready for a review!

C = [[1,2],[3,4]]
D = [[2,0],[1,2]]

E = [[0,0],[0,0]]

for i in range(len(C)):
    for j in range(len(D)):
        E[i][j] = 0
        for k in range(len(D)):
            E[i][j] += C[i][k] * D[k][j]

print(E)