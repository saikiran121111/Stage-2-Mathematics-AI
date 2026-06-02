from statistics import quantiles

import numpy as np



val = np.array([2,3]) # A vector is just a single matrix

print(val)

# dot product( Used it for total calculations like bill etc)

# The "Dot Product" sounds scary, but it is just a scoring system. You match items up, multiply them, and add the total.
#
# Real-World Example:
# Imagine going to the grocery store.
#
# Vector A (Quantities): You buy [2, 3] (2 apples, 3 bananas).
#
# Vector B (Prices): They cost [10, 5] (10 rupees per apple, 5 rupees per banana).
#
# How do you find the total bill?
#
# Multiply the apples: 2 * 10 = 20
#
# Multiply the bananas: 3 * 5 = 15
#
# Add them together: 20 + 15 = 35.
#
# Congratulations, you just calculated a Dot Product!


quantities = np.array([2,3]) # (2 apples, 3 bananas)
prices = np.array([10,5]) # (10rs for each apple, 5rs for each banana)

total_bill = np.dot(quantities,prices)
# Or you can use: total_bill = quantities @ prices which is used for matrix multiplication

print(total_bill) # Total bill is 35