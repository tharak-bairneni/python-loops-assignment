#TASK 1: Create Array & Basic Math

import numpy as np
import time

# Create NumPy array
temps_celsius = np.array([22, 25, 28, 24, 26])

# Convert to Fahrenheit (Vectorized operation)
temps_fahrenheit = temps_celsius * 1.8 + 32

# Calculate average Fahrenheit (rounded to 1 decimal)
avg_fahrenheit = round(np.mean(temps_fahrenheit), 1)

print("\ntask1--Output\n")
print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)
print("Average Fahrenheit:", avg_fahrenheit)

 #TASK 2: Shape & Statistics

scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print("\ntask2--Output\n")
print("Shape:", scores.shape)
print("Total elements:", scores.size)

highest = np.max(scores)
lowest = np.min(scores)
score_range = highest - lowest

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Range:", score_range)
 
#TASK 3: Performance Comparison
 
# Create NumPy array
np_array = np.arange(1, 50001)

# Create Python list
py_list = list(range(1, 50001))

# NumPy timing
start_np = time.time()
np_sum = np.sum(np_array)
end_np = time.time()
np_time = end_np - start_np

# Python timing
start_py = time.time()
py_sum = sum(py_list)
end_py = time.time()
py_time = end_py - start_py

# Calculate speed difference
speed_factor = py_time / np_time

print("\ntask3--Output\n")
print("NumPy sum:", np_sum)
print("Python sum:", py_sum)
print("NumPy time:", format(np_time, ".4f"), "seconds")
print("Python time:", format(py_time, ".4f"), "seconds")
print("NumPy is", round(speed_factor, 1), "x faster\n")