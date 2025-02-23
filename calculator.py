class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b

calc = Calculator()
print("Addition:", calc.add(10, 10))
print("Subtraction:", calc.subtract(10, 7))
print("Multiplication:", calc.multiply(10, 2))
print("Division:", calc.divide(9, 5))