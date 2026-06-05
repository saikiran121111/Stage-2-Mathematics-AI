# The Real-Life Story: The Biryani Delivery
# Imagine you track the delivery times for 1,000 Swiggy orders of Biryani in Hyderabad.
# On the restaurant's app, the average delivery time says 30 minutes.
# If you look at the actual data for all 1,000 deliveries, here is what happens:
# The Average (The Peak): Most of the deliveries (say, 700 of them) happen right around the 25 to 35-minute mark.
# Drivers are on time, traffic is normal.
# The Fast Extremes (Left Slope): A tiny handful of deliveries happen in exactly 10 minutes (maybe the customer lives right next door).
# This is very rare.
# The Slow Extremes (Right Slope): A tiny handful of deliveries take 60 minutes (heavy rain, flat tire). This is also very rare.

# Visualizing the Shape:
# If you drew a dot on a graph for every single delivery time,
# the dots would naturally pile up in the middle because average events happen most often.
# The dots would look very thin on the edges because extreme events are rare.
# If you draw a line over the top of this pile of dots, you get a symmetrical hill that looks like a church bell:

                 #                /\
                 #               /  \
                 #              /    \
                 #             /      \
                 #            /        \
                 # -----------          ---------
#
# The highest peak in the dead center is the Average (Mean).
#
# The width of the hill is the Standard Deviation (how much the delivery times vary due to traffic).
# If the hill is very narrow, the drivers are incredibly consistent. If the hill is wide, the delivery times are unpredictable.

# Higher the hill and it looks like a single bell the better chance of prediction

# Why do AI Engineers actually care?
# In AI, we love the Bell Curve for one simple reason: It represents predictability.
#
# If an AI model knows your data fits into a clean Bell Curve, it can make incredibly accurate guesses.
# It can look at a 30-minute delivery average and say, "I am 95% confident this next Biryani will arrive between 20 and 40 minutes."
# If data doesn't look like a bell curve—for instance, if it has two peaks or is totally flat—the AI struggles
# to learn the patterns because the "normal" baseline keeps shifting.

# Coding Example: Simulating Swiggy Deliveries
# We use np.random.normal(loc, scale, size) to generate random data that perfectly fits a bell curve.
#
# loc: The center peak (The Mean/Average)
#
# scale: The width of the hill (The Standard Deviation/Spread)
#
# size: How many data points you want to create

import numpy as np

# Let's simulate 1,000 Biryani deliveries
# Average time = 30 mins, Standard Deviation = 5 mins
delivery_times = np.random.normal(loc=30, scale=5, size=1000)

# Check the average of our simulated deliveries
print("Simulated Average:", np.mean(delivery_times))
# Output will be very close to 30.0 (e.g., 30.08)