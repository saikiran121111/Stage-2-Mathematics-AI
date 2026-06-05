import numpy as np

employees = [
  (1, 'Alice',   'IT',      'Mumbai',    50000),
  (2, 'Bob',     'HR',      'Delhi',     60000),
  (3, 'Charlie', 'IT',      'Mumbai',    55000),
  (4, 'Diana',   'Finance', 'Chennai',   70000),
  (5, 'Eve',     'IT',      'Delhi',     45000),
  (6, 'Frank',   'HR',      'Hyderabad', 80000)
]

# Level 1 — Absolute Basics:
# Extract all the salaries from the employees dataset into a simple list or NumPy array.
# Calculate and print the Mean salary using NumPy.
# Expected Output: 60000.0

numArr = np.array(employees)

maths_columns = numArr[:,[4]].astype(float) # [:,[4]] : takes all rows , [4] we are taking 4th column here and converting it to float

print("Average Salary:", np.mean(maths_columns))

# Level 2 — Real-life Application (Identifying Outliers):
# Calculate the Standard Deviation of the salaries.
# Print it out cleanly.
# Expected Output: 11902.380714238083 (This tells HR that most employee salaries typically drift about ₹12,247 away from the average).

print("Standard Deviation (in Rupees):", np.std(maths_columns))

# Level 3 — Interview Trap (The Manual Bias / Degrees of Freedom):
# In interviews, they will ask you about ddof (Delta Degrees of Freedom). By default, np.std() assumes you are calculating the standard deviation
# for an entire company (a population). But if your data is just a small sample of a larger company,
# the math needs a slight correction to stay accurate.
#
# Calculate the standard deviation of the employee salaries again, but this time pass the parameter ddof=1 inside np.std(). Print the result.
# Expected Output: 13038.404810405298

print('Standard Deviation (in Ruppees):', np.std(maths_columns,ddof=1))

# Level 4 — Mastery (Z-Score - The Core AI Formula):
# In machine learning, models hate processing raw numbers like 50000 or 80000 because big numbers mess up the math.
# We use a Z-Score formula to scale everything down to small numbers (usually between -3 and 3).
# The formula for a single salary is Z-Score = Salary - Mean / Standard Deviation
# 'Write a Python script (using your calculated Mean and standard deviation from Level 1 & 2) to find the Z-score for Frank's salary (80,000).
# Print Frank's Z-score.Expected Output: 1.6803361 (This tells our AI model that Frank makes 1.63 standard deviations more than the company average!)


frank_salary = numArr[[5],[4]].astype(float)

mean = np.mean(maths_columns)

standard_deviation = np.std(maths_columns)

z_score = (frank_salary - mean)/standard_deviation

print(z_score.astype(float))