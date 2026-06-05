# Let's start with the absolute basics of how AI models think about uncertainty: Mean, Variance, and Standard Deviation.

# The Concept: Targets and Spreads
# Mean (Average): The middle ground. If you add up all employee salaries and divide by the number of employees, you get the Mean.
#
# Variance: How wildly scattered the data is.
#
# If everyone at Accenture Hyderabad makes roughly the same salary, the variance is low.
#
# If some people make ₹30,000 and others make ₹30,00,000, the data is all over the place, meaning the variance is high.
#
# Standard Deviation: Variance is calculated using squared numbers (which makes the units weird).
# Standard Deviation is just the square root of variance, bringing the number back into real-world units (like Rupees) so humans can easily read it.


import numpy as np

salaries = [50000, 60000, 55000, 45000]

print("Average Salary:", np.mean(salaries))
print("Data Scatter (Variance):", np.var(salaries))
print("Standard Deviation (in Rupees):", np.std(salaries))

# Simple terms
# Mean is to find average
# Variance is used for optimizations and calculus mostly for formulas and evaluations which is squared
# deviation is basically a square root of variation which is in human readable format
# Variace and deviation are used to find how volatile the prediction is
# E.G:
# Keep it very real:
# Student exam scores
# Mean = class average (e.g., 70).
# Low standard deviation → most students got around 70 (scores clustered).
# High standard deviation → some got 20, some got 95 (big spread).
# In AI, similar idea for model predictions: are they consistently close to truth, or sometimes very off?
# Weather temperatures
# Same average temperature in two cities (say 25°C).
# City A: 24, 25, 26, 25 → low std → weather is stable, easy to predict.
# City B: 10, 40, 15, 35 → high std → weather is wild, hard to predict.
# Stock market
# Two stocks both average 10% yearly return.
# Stock A: returns mostly between 8–12% → low std → safe/stable.
# Stock B: returns -30%, +50%, -10%, +40% → high std → risky/volatile.
