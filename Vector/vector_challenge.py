import numpy as np

# Level 1 — Absolute Basics:
#
# Create a vector A: [4, 5, 6]
#
# Create a vector B: [1, 2, 3]
#
# Calculate the dot product using np.dot() and print the result.
#
# Expected Output: 32 (Because: 41 + 52 + 6*3 = 4 + 10 + 18 = 32)

vecA = np.array([4,5,6])
vecB = np.array([1,2,3])

dotprod = np.dot(vecA,vecB)
print(dotprod)

# Level 2 — Real-life (Employee Scoring):
#
# Let's evaluate Bob from your dataset. Create a vector for Bob's skills: [80, 90, 70] (Code Quality, Communication, Punctuality).
#
# Create a vector for the Company Weights: [0.5, 0.3, 0.2] (Code is worth 50%, Comm 30%, Punc 20%).
#
# Calculate Bob's final performance score using the @ symbol.
#
# Expected Output: 81.0

vecA = np.array([80,90,70]) # Code Quality, Communication, Punctuality
vecB = np.array([0.5, 0.3, 0.2]) # worth 50%, comm 30%, punc 20%

overall_performance = vecA @ vecB

print(overall_performance)

# Level 3 — Interview Trap (The Size Mismatch):
#
# The golden rule of the Dot Product: Both vectors must have the exact same number of items.
#
# Create vector X: [1, 2, 3] (3 items)
#
# Create vector Y: [4, 5] (2 items)
#
# Try to calculate the dot product. It will crash!
#
# Wrap it in a try...except ValueError: block. In the except block, print "Interview Trap: Vectors must be the same size!"
#
# Expected Output: Interview Trap: Vectors must be the same size!

vectA = np.array([1, 2, 3])
vectB = np.array([4, 5])

try:
    total_cal = np.dot(vectA,vectB)
except ValueError:
    print('Interview Trap: Vectors must be the same size!')

# Level 4 — Mastery (Under the Hood):
# AI Engineers need to know how the math actually works, not just how to call a NumPy function.
#
# Create vector C: [10, 20, 30]
#
# Create vector D: [2, 2, 2]
#
# Without using NumPy (pretend you only have standard Python), write a for loop that calculates the dot product of C and D.
#
# Hint: Create a variable total = 0, loop through the index of the lists, multiply C[i] * D[i], and add it to total.
#
# Print your manual total.
#
# Expected Output: 120

vecC = np.array([10,20,30])
vecD = np.array([2,2,2])
total = 0
for i,j in zip(vecC,vecD):
    mult = i*j
    total = total+mult

print(total)