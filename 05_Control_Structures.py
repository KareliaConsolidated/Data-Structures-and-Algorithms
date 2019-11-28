# Exercise :
# Write smallest_positive which is a function that finds the smallest positive number in a list.
def smallest_positive(num_list):
	smallest_pos_num = None
	for num in num_list:
		if num > 0:
			if smallest_pos_num == None or smallest_pos_num > num:
				smallest_pos_num = num
	return smallest_pos_num

# Test Cases
print(smallest_positive([4, -6, 7, 2, -4, 10])) # 2
print(smallest_positive([0.2, 5, 3, -.01, 7, 7, 6])) # 0.2

# The data structure format is:

#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

courses = {
    'spring2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'fall2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }

# In this exercise, you will need to complete the function 
# when_offered(courses, course). This function accepts a "courses" 
# data structure and a "course" string. 
# The function should return a list of strings representing the semesters 
# when the input course is offered. See the two test cases below for examples 
# of correct results.

def when_offered(courses, course):
	semesters = []
	for semester in courses:
		if course in courses[semester]:
			semesters.append(semester)
	return semesters

print(when_offered(courses, 'bio893')) # []

print(when_offered(courses, 'cs101')) # ['spring2020', 'fall2020']