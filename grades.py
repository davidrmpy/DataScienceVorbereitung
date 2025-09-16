grades = {"Anna":5.1, "Paul":1.4, "David":6.0, "Gloria":4.4}
grades1 = {"Anna":5, "Paul":1, "David":6, "Gloria":4}

print(len(grades1))

average_grades = sum(grades.values()) / len(grades)
print(sum(grades.values()) / len(grades))
print(sum(grades1.values()) / len(grades1))


print("The average grade is", average_grades)


for student, grade in grades.items():
    if grade >= 4:
        print(f"{student} Passed")
    else:
        print(f"{student} Failed")
