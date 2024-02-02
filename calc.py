def add(a, b):
    """Addition function"""
    return a + b

def subtract(a, b):
    """Subtraction function"""
    return a - b

def multiply(a, b):
    """Multiplication function"""
    return a * b

def divide(a, b):
    """Division function"""
    if b == 0:
        raise ValueError("Can not divide by zero!!")
    
    return a / b

