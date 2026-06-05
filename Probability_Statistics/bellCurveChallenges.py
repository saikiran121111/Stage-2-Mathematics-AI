# Level 1 — Absolute Basics (The Happiness Score):
# Use np.random.normal() to create an array of 5,000 employee satisfaction scores.
# Set the mean (loc) to 7.5 and the standard deviation (scale) to 1.0.
# Calculate and print the np.mean() of your new array to prove it sits right at the peak.
# Expected Output: A number extremely close to 7.5 (e.g., 7.49... or 7.51...)

import numpy as np

happiness_score = np.random.normal(loc=7.5,scale=1.0,size=5000)

print("Simulated Average:", round(np.mean(happiness_score),2))

# Level 2 — Real-life Application (Finding Elite Earners):
# Let's simulate a massive expansion at Accenture Hyderabad. Generate a normal distribution of 10,000 simulated software engineer
# salaries with a mean of 60000 and a standard deviation of 10000.
# Write code to count how many of these simulated employees make an elite salary greater than or equal to 80000 (Frank's bracket).
# Hint: You can filter and sum a NumPy array instantly using np.sum(salaries >= 80000).
# Print the final headcount.
# Expected Output: Roughly between 210 and 250 employees (This represents the top ~2.3% tail of your bell curve!).

finding_elite_earners = np.random.normal(loc=60000,scale=10000,size=10000)

print(f'Salaries greater than 80k: {np.sum(finding_elite_earners >= 80000)}')

# Level 3 — Interview Trap (The CEO Salary Lie):
# Interviewers love testing your understanding of Mean vs Median on a distribution. If a dataset has a wild outlier,
# the mean completely changes, but the median stands strong.
# Create a simple array of 5 typical employee salaries: [50000, 60000, 55000, 45000, 80000].
# Calculate and print its np.mean() and np.median(). (They will be very close).
# The Trap: Add a single massive outlier to that array—the CEO's salary of 2000000 (20 Lakhs).
# Calculate the new Mean and new Median. Print them both out to see who tells the truth about the "average" worker.
# Expected Output: * New Mean: 381666.6666666667 (Completely distorted!)
# New Median: 57500.0 (Still accurately represents the middle worker!)

emp_salaries = np.array([50000, 60000, 55000, 45000, 80000, 2000000])

print(f'Average Salary: {np.mean(emp_salaries)}')
print(f'Median Salary: {np.median(emp_salaries)}')

# Level 4 — Mastery (Standard Scaling for AI):
# Before feeding data distributions into a neural network, AI Engineers must convert them into a Standard Normal Distribution
# (meaning the mean becomes exactly 0 and the standard deviation becomes exactly 1).
# We do this by calculating the Z-score for the entire dataset at once.
#
# Generate an array of 1,000 raw data values: raw_data = np.random.normal(loc=150, scale=25, size=1000).
#
# Transform the entire array using this vectorized formula: standardized = (raw_data - np.mean(raw_data)) / np.std(raw_data)
#
# Print the np.mean(standardized) and np.std(standardized) of your new array.
#
# Expected Output: Mean will be extremely close to 0.0 (often written in scientific notation like 1.23e-16),
# and Standard Deviation will be exactly 1.0.

raw_data = np.random.normal(loc=150, scale=25, size=1000)
# Z-score formula
# data-mean/standard deviation
standardized = (raw_data - np.mean(raw_data)) / np.std(raw_data)

print(np.mean(standardized))
print(np.std(standardized))

# Answering Your Question: Why is it showing 8.246736626915663e-16?
# Don't panic! Your math is 100% correct.
# What you are seeing is an interview classic called Floating-Point Precision Limitation.
# In computer systems,
# numbers are stored in binary (0s and 1s). Just like a calculator cannot perfectly represent 1/3
# without writing $0.33333333...$ infinitely, a computer cannot perfectly store certain decimal numbers in binary.
# That e-16 at the end is Scientific Notation. It means "move the decimal point 16 places to the left.
# "If we write out your output fully, it looks like this:0.0000000000000008246736626915663
# For an AI Engineer,
# this number is practically zero. Because of tiny micro-rounding errors when scaling 1,000 numbers simultaneously,
# the computer gets infinitely close to 0, but leaves a microscopic trace at the very end.
# If you want to clean it up for printing, you can simply round it: print(round(np.mean(standardized), 2)),
# which will output a clean 0.0.

