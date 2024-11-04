# add
def add(n, m):
    return n + m

# subtract
def subtract(n, m):
    return n - m

# multiply
def multiply(n, m):
    return n * m

# divide
def divide(n, m):
    if m == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return n / m