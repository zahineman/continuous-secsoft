def add(a, b):
    return int(a) + int(b)

def subtract(a, b):
    return int(a) - int(b)

def multiply(a, b):
    return int(a) * int(b)

def divide(a, b):
    if b == 0:
        raise Exception("Denominator/Divisor must be non-zero")
    else:
        return int(a) / int(b)