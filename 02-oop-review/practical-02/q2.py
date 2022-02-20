# Create SoftwareDeveloper & ProductOwner classes which inherit from 
# the Employee class. SoftwareDeveloper class has one additional
# attribute called prog_lang. ProductOwner has one additional attribute
# called employees & three methods which add, remove & show all
# employees managed by the Product Owner. Note: employees is a list of
# SoftwareDeveloper objects.
#
# Use the three SoftwareDeveloper objects & one ProductOwner object
# provided in the main function to display the expected output.

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
# Write your solution here. 



# Don't modify anything below this line.
def main():
    sft_dev_one = SoftwareDeveloper('Alfredo', 'Boyle', 50000, 'C#')
    sft_dev_two = SoftwareDeveloper('Malik', 'Martin', 55000, 'JavaScript')
    sft_dev_three = SoftwareDeveloper('Livia', 'Martin', 75000, 'Kotlin')
    prdt_owr = ProductOwner('Lillian', 'Cunningham', 100000, [sft_dev_one, sft_dev_two])
    # Add sft_dev_three to the list of employees
    prdt_owr.employees.append(sft_dev_three)
    # Remove sft_dev_one from the list of employees
    prdt_owr.employees.remove(sft_dev_one)
    # Hint: Look up Python list methods
    prdt_owr.show_employees()

if __name__ == '__main__':
    main()
    
# Expected output:

# Malik Martin
# Livia Martin
