# Baye's Theorem is nothing but probability of finding if something happens by taking the clue's

# Eg:

# Imagine you wake up, look out your window in Hyderabad, and see Clouds.
# You want to know: "What is the actual chance that it will Rain today, just because it is Cloudy?"
#
# To figure this out, you look at your past weather diary which tells you three simple facts:
#
# Overall chance of Rain: On any random day of the year, it only rains 10% of the time.
#
# Clouds when it Rains: Out of all the days it actually rained in the past, 90% of them started with clouds.
#
# Overall chance of Clouds: On any random day of the year, 30% of the days are cloudy (sometimes it's just cloudy but doesn't rain).
#
# Bayes' Theorem is just a recipe that takes those 3 facts and cooks them into the exact answer you want.

# Maths formula
#             P(B|A) * P(A)
# P(A|B) = ───────────────────
#                  P(B)

# General explaination formula
#                                (Clouds when it Rains) × (Overall chance of Rain)
# Chance of Rain given Clouds = ───────────────────────────────────────────────────
#                                                Overall chance of Clouds

# Let's plug our simple diary numbers into this recipe:
#
# Top Part: 0.90 (Clouds when it Rains) × 0.10 (Overall Rain) = 0.09
#
# Bottom Part: 0.30 (Overall Clouds)
#
# Final Answer: 0.09 / 0.30 = 0.30 (or 30%)
#
# So, even though you see clouds, there is only a 30% chance it will actually rain.
#
# Translating This Directly Into Code
# When we write this in Python, we use clear, human-readable variable names so the code documents itself. Read this line-by-line:

def calculate_rain_chance(clouds_when_raining, overall_rain, overall_clouds):
    # 1. Calculate the top part of our fraction
    top_part = clouds_when_raining * overall_rain

    # 2. Divide by the bottom part
    final_probability = top_part / overall_clouds

    return final_probability


# Let's test it with our weather diary numbers:
chance = calculate_rain_chance(
    clouds_when_raining=0.90,
    overall_rain=0.10,
    overall_clouds=0.30
)

print(f"Chance of rain is: {chance * 100}%")
# Output: Chance of rain is: 30.0%