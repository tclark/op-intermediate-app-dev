"""Answer the questions below using the LEGB rule."""


num = 7

def func():
    count = 10
    def print_seven():
        extra = 2
        for _ in range(count + extra): # A
            print(num) # B
    return print_seven

f = func()
f()

# Answer the questions below.

#Q1: At the line marked A, describe how the interpreter finds the name count.
#Q2: At the line marked A, describe how the interpreter finds the name extra.
#Q3:  At the line marked B, describe how the interpreter finds the name num.
