import numpy as np

# The Concept: The Stubborn Arrows
# Forget the terrifying mathematical equations you see online. Let's look at this purely visually.
#
# A Vector is an Arrow: It points in a specific direction on a graph.
#
# A Matrix is a Transforming Machine: When you multiply a matrix by an arrow,
# the machine usually knocks the arrow off its path—it rotates it and stretches it out.
#
# However, for every matrix machine, there are a few special, stubborn arrows.
# When these stubborn arrows go through the machine, they refuse to rotate.
# They stay pointing in the exact same direction on their original straight line.
# The machine is only allowed to stretch them out or squish them shorter.
#
# Eigenvector: The stubborn arrow that refuses to rotate.
#
# Eigenvalue: The "Stretch Factor." It's just a number telling you how much that stubborn arrow stretched.
# (e.g., If the arrow became 3 times longer, its Eigenvalue is 3).
#
# Why do AI Engineers care?
# In AI, datasets have massive amounts of columns (features).
# We turn data into a matrix machine, find the eigenvectors with the largest eigenvalues (biggest stretch factors),
# and throw away the rest. This lets us compress thousands of columns into just a few important ones without losing information.
# You will use this exact trick for Principal Component Analysis (PCA) in Stage 3.


# A simple 2x2 square matrix machine
matrix = np.array([[2, 0],
                   [0, 3]])

eigenvalue, eigenvector = np.linalg.eig(matrix)

print(f'EigenValue: {eigenvalue}  EigenVector : {eigenvector}')