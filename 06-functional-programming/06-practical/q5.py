# Create a set comprehension which returns the breed of dogs who are not
# aggressive. Use the set comprehension to display the expected output.

class Dog:
    def __init__(self, breed, is_aggressive):
        self.breed = breed
        self.aggressive = is_aggressive

def main():
    dogs = [
        Dog('American Pit Bull Terrier', True),
        Dog('Cavalier King Charles Spaniel', False),
        Dog('Cavalier King Charles Spaniel', False),
        Dog('Labrador Retriever', False),
        Dog('Rottweiler', True),
        Dog('Shih Tzu', False)
    ]

    # Write your solution here

if __name__ == '__main__':
    main()

# Expect output:

# {'Shih Tzu', 'Labrador Retriever', 'Cavalier King Charles Spaniel'}
