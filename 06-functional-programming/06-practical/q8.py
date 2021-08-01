# Using the randrange function, create a list comprehension called exam_scores
# which generates 10 numbers between 1 & 100. Use exam_scores, the filter function
# & a lambda function to return all items ≥ 80.
#
# Note: your outputs will be different than what is shown below.

from random import randrange

exam_scores = # Write your solution here
a_grade_range_exam_scores = filter('''Write your lambda function here''')
print(f'Exam scores: {exam_scores}')
print(f'A grade range exam scores: {list(a_grade_range_exam_scores)}')

# Expected output:
# Exam scores: [52, 51, 82, 11, 16, 19, 10, 91, 59, 58]
# A grade range exam scores: [82, 91]
