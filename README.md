# Stage-2-Mathematics-AI

#I know "Linear Algebra" sounds terrifying.
# But in AI, it is just a fancy way of saying
# "organizing numbers in lists and grids so the computer can do math on them really fast."

#1. What is a Vector?
#A vector is just a 1-dimensional list of numbers. That's it.
#In AI, if we want to represent our employee Alice using only her numerical data (ID: 1, Salary: 50000),
# her "vector" is just [1, 50000].

#NumPy Code: alice_vector = np.array([1, 50000])

# 2. What is a Matrix?
# A matrix is a 2-dimensional grid (or table) of numbers. If a vector is a single row,
# a matrix is the whole spreadsheet. If we put Alice and Bob's numerical data together, we get a matrix.
#
# NumPy Code:
#
# Python
# employees_matrix = np.array([
#     [1, 50000],  # Alice
#     [2, 60000]   # Bob
# ])

# 3. What is a Dot Product?
# This is the single most important math operation in AI. Neural networks run on millions of dot products.
# A dot product takes two vectors, multiplies their matching items together, and then adds those results up into a single number.
#
# Imagine Vector A is [Number of Hours Worked, Hourly Rate] and Vector B is [2, 500].
# The Dot Product multiplies the first items together, multiplies the second items together, and adds them: (2 * 500) = 1000.
#
# NumPy Code:
