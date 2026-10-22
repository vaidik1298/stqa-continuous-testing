
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def modulus(a, b):
    """Return the remainder after dividing a by b."""
    if b == 0:
        raise ZeroDivisionError("Cannot calculate modulus by zero")
    return a % b


def power(a, b):
    """Raise a to the power b."""
    return a ** b


def average(a, b):
    """Return the average of two numbers."""
    return (a + b) / 2


def maximum(a, b):
    """Return the larger of two numbers."""
    return max(a, b)


def minimum(a, b):
    """Return the smaller of two numbers."""
    return min(a, b)


def percentage(part, whole):
    """Return part as a percentage of the whole."""
    if whole == 0:
        raise ValueError("The whole cannot be zero")
    return (part / whole) * 100


def absolute_difference(a, b):
    """Return the non-negative difference between two numbers."""
    return abs(a - b)


def square(a):
    """Return the square of a number."""
    return a ** 2


def cube(a):
    """Return the cube of a number."""
    return a ** 3
