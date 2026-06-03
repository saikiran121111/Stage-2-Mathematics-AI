from logging import exception

import numpy as np
from numpy import linalg

# Level 1 — Absolute Basics:
#
# Create this matrix: [[4, 0], [0, 5]]
#
# Find the eigenvalues using np.linalg.eig() and print them.
#
# Expected Output: [4. 5.]


matrix = np.array([[4, 0], [0, 5]])


eigenValue,eigenVector = np.linalg.eig(matrix)

print(f'EigenValue : {eigenValue} EigenVector : {eigenVector}')

# Level 2 — Real-life Application (PCA Trend Detection):
#
# Imagine an employee dataset comparing Experience vs Performance scores. We create a "Covariance Matrix" of the data: [[10, 2], [2, 5]]
#
# Find the eigenvalues.
#
# Use np.max() to find and print only the largest eigenvalue (the most dominant data trend).
#
# Expected Output: 10.701562118716424

covarienceMat = np.array([[10, 2], [2, 5]])


eigenValue,eigenVector = np.linalg.eig(covarienceMat)

print(f'Max Eigen Value : {np.max(eigenValue)}')


# Level 3 — Interview Trap (The Square Matrix Rule):The Golden Interview Rule:
# Only perfectly square matrices ($2 \times 2, 3 \times 3$, etc.)
# can have eigenvalues and eigenvectors. If a matrix is rectangular, the math breaks.Create a 3x2 matrix:
# [[1, 2], [3, 4], [5, 6]]
# Try running np.linalg.eig() on it.
# It will crash.Wrap your code in a try...except block (catch ValueError or NumPy('s LinAlgError). '
# 'In the except block, print: "Interview Trap: Matrix must be square!"Expected Output: Interview Trap: Matrix must be square!)

matrix = np.array([[1, 2], [3, 4], [5, 6]])

try:
    eigenValue,eigenVector = np.linalg.eig(matrix)
except Exception:
    print("Interview Trap: Matrix must be square!")


# Level 4 — Mastery (Eigendecomposition/Rebuilding):
#
# Advanced AI libraries break down a matrix into its core elements and rebuild it to save computing power. Let's do that manually.
#
# Create Matrix A: [[3, 1], [0, 2]]
#
# Find its eigenvalues and eigenvectors.
#
# Convert the eigenvalues into a diagonal matrix using: L = np.diag(eigenvalues)
#
# Rebuild Matrix A using this exact multiplication formula: eigenvectors @ L @ np.linalg.inv(eigenvectors)
#
# Print the rebuilt matrix.
#
# Expected Output: ```text
# [[3. 1.]
# [0. 2.]]
print('#########################Level4#########################')
matA = np.array([[3,1],[0,2]])

eigenValue,eigenVector = np.linalg.eig(matA)

L = np.diag(eigenValue) # Converts the Eigen Values to diagonal Matrix

rebuildingMatrix = eigenVector @ L @ np.linalg.inv(eigenVector)

print(rebuildingMatrix)

# The main reason we do this inversion because to raise the matrix to maximum power
# Like multiplying matrix by itself 100 times will burn the CPU down
# So mathematicians figured it out that we simply multiply the diagonal of eigen value instead of general matrix
# This will automatically makes matrix to high power with less calculations
# Same output lightning fast !!!