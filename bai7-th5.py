import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details =[('james', 5, 48.5), ('Nail', 6, 52.5),('paul', 5, 42.10), ('pit', 5, 40.11)]
# create a structured array
students = np.array(students_details, dtype=data_type)
print("original array:")
print(students)
print("Sort by height")
print(np.sort(students, order='height'))
 
