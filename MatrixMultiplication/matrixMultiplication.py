# The Secret Definition:
# Matrix-Vector multiplication is literally just doing multiple dot products back-to-back.
#
# Imagine you have a table (Matrix) representing 3
# employees, where each row holds their [Technical Skill, Communication] score.
# You have a single vector representing the company's evaluation weights [0.7, 0.3].
#
# When you multiply the Matrix by the Vector, the machine takes the first row of the matrix,
# does a dot product with your weights vector, and outputs a single number (Employee 1('s total score). '
# 'Then it moves to the second row, does a dot product, and outputs the next number.)

# The Golden Rule of Shapes:
# For this to work, the length of the matrix rows must match the length of the vector.
#
# If your matrix has a shape of (3, 2) (3 employees, 2 skills each).
#
# Your vector must have a shape of (2,) (2 weights).
#
# The Result: You fed 3 employees in, so you get a vector of shape (3,) out!

# Matrix-Matrix Multiplication
# Now that you can multiply a matrix by a single vector, let's look at the ultimate level: multiplying a matrix by another matrix.
#
# Don't let the name intimidate you. As a developer, think of it this way: Matrix-Matrix multiplication is just running multiple Matrix-Vector multiplications side-by-side at the exact same time.
#
# The Real-Life Scenario
# Imagine we have our 3 employees with their [Base Salary, Extra Projects] data.
# Instead of testing just one bonus scheme, HR wants to test two different bonus plans simultaneously to compare the total costs.
#
# Plan 1: Keep 100% of base, pay ₹1,000 per project.
#
# Plan 2: Keep 100% of base, pay ₹2,000 per project.
#
# Instead of writing complex nested loops, we put both plans into a single matrix and multiply them using @.
#
# The Golden Rule of Shapes (Interview Favorite)
# If Matrix A has a shape of (3, 2) (3 employees, 2 metrics) and Matrix B has a shape of (2, 2) (2 metrics, 2 plans):
#
# Look at the inner numbers: (3, 2) @ (2, 2). They match!
#
# Look at the outer numbers: (3, 2) @ (2, 2). The output will automatically be a (3, 2) matrix (3 employees, 2 final plan scores each).