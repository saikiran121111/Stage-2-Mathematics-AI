# Level 1 — Absolute Basics (The Weather Bot):
# Copy the calculate_rain_chance function structure above into your script.
# Change the numbers to a new city's weather:
# Overall chance of rain is 20% (0.20)
# It is cloudy when it rains 80% of the time (0.80)
# Overall chance of clouds is 40% (0.40)
# Run the function and print the result.
# Expected Output: 0.4 (40% chance of rain)

def calculate_rain_chance(overall_chance_rain,cloudy_when_rain,overall_chance_cloud):

    toppart = cloudy_when_rain * overall_chance_rain

    finalprediction = toppart/overall_chance_cloud

    return finalprediction

print(f'Chance of rain is : {round(calculate_rain_chance(0.20,0.80,0.40)*100,2)}%')

# Level 2 — Real-life Application (The Biryani Predictor):
# Let's change the variable names to represent a fun office scenario. Write a function called chance_of_friday_given_biryani.
# Scenario: You walk into the Accenture Hyderabad cafeteria and smell Biryani. You want to know what the chance is that today is Friday.
# Overall baseline chance of any workday being Friday is 20% (0.20 because it's 1 out of 5 workdays).
# On Fridays, the cafeteria serves Biryani 90% of the time (0.90).
# On any random workday overall, the cafeteria serves Biryani 30% of the time (0.30).
# Calculate the probability that it is Friday given that there is Biryani.
# Expected Output: 0.6 (60% chance it's Friday!)

def chance_of_friday_biryani(chance_of_wd_friday,friday_cafe_serves_biryani,random_wd_biryani):

    toppart = chance_of_wd_friday * friday_cafe_serves_biryani

    finalprediction = toppart/random_wd_biryani

    return finalprediction

print(f'Chance of today being friday is : {round(chance_of_friday_biryani(0.20,0.90,0.30)*100,1)}%')

# Level 3 — Interview Trap (The Ghost Town Bug):
# What if you check for something that never happens? For example, what if the overall chance of seeing clouds is 0.0?
# Your code will attempt to divide by 0 and crash with a ZeroDivisionError.
# Copy your function from Level 1, but add an if statement to check if the bottom number (overall clouds) is exactly 0.0. If it is 0.0,
# safely return 0.0 instead of dividing.
# Test your function by passing 0.0 as the overall chance of clouds.
# Expected Output: 0.0 (instead of crashing your application!)

def calculate_rain_chance(overall_chance_rain,cloudy_when_rain,overall_chance_cloud):

    toppart = cloudy_when_rain * overall_chance_rain

    if overall_chance_cloud != 0:
        finalprediction = toppart/overall_chance_cloud
    else:
        return 0
    return finalprediction

print(f'Chance of rain is : {round(calculate_rain_chance(0.20,0.80,0)*100,2)}%')


# Level 4 — Mastery (The Spammer Alert):
# Let's write a generic, reusable Bayes' Theorem function that can handle any AI problem. Name your parameters:
# probability_b_given_a, probability_a, and probability_b.

# Scenario: An AI spam filter is checking an email containing the word "FREE".
# Overall chance an email is Spam is 5% (0.05).
# If an email is Spam, the chance it contains the word "FREE" is 80% (0.80).
# Across all emails (both safe and spam), the word "FREE" appears 10% of the time (0.10).
# Pass these numbers into your generic function to find the probability that the email is genuinely Spam.
# Expected Output: 0.4 (Even though it has the word "FREE", there is only a 40% chance it's actual spam because spam is rare overall).

def spam_alert(probability_b_given_a,probability_a,probability_b):

    topPart = probability_b_given_a * probability_a

    if probability_b != 0:
        finalProbability = topPart/probability_b
    else:
        return 0
    return finalProbability

print(f'Spam Probability is : {round(spam_alert(0.80,0.05,0.10)*100,1)}')
