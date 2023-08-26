def student_grade(name, grade):
    return "{} received {}% on the exam".format(name, grade)

print(student_grade("Jaidi", 80))
print(student_grade("Leo", 92))
print(student_grade("Usman", 70))

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)