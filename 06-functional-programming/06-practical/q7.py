# Using the uuid4 function, generate a random UUID called rand_uuid. Use
# rand_uuid, the map function & a lambda function to return an uppercase
# rand_uuid. 
#
# Note: your outputs will be different to what is shown below since the 
# UUID value will be different.

from uuid import uuid4

rand_uuid = # Write your solution here
upper_rand_uuid = ''.join(map('''Write your lambda function here'''))
print(f'Random UUID: {rand_uuid}')
print(f'Uppercase random UUID: {upper_rand_uuid}')

# Expected output:

# Random UUID: 58a641f1-ac6a-4a5d-ab31-302af8b2dfc4
# Uppercase random UUID: 58A641F1-AC6A-4A5D-AB31-302AF8B2DFC4
