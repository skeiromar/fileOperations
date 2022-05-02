

def operation(num1, operation, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return 'Invalid operation'

class Arithmetic:
    def __init__(self, num1, operation, num2):
        self.num1 = num1
        self.operation = operation
        self.num2 = num2

    def calculate(self):
        if self.operation == '+':
            return self.num1 + self.num2
        elif self.operation == '-':
            return self.num1 - self.num2
        elif self.operation == '*':
            return self.num1 * self.num2
        elif self.operation == '/':
            return self.num1 / self.num2
        else:
            return 'Invalid operation'