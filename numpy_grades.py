import numpy as np

grades = {"Anna": 5.1, "Paul": 1.4, "David": 6.0, "Gloria": 4.4}

grades_list = list(grades.values())

grades_array = np.array([grades_list])

average = np.mean(grades_array)

print(f"Average grade is {average}")

