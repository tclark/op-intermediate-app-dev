# Implement the Calculator class below using the Factory Method pattern.




class Calculator:
    pass

if __name__ == '__main__':
    calc = Calculator()
    print(calc.calculate(1, '+', 1))  # should print 2
    print(calc.calculate(2, '*', 3))  # should print 6
    print(calc.calculate(4, '-', 3))  # should print 1
    print(calc.calculate(8, '/', 2))  # should print 4.0
