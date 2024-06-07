def factorial(n):
    if n < 0:
        raise ValueError("debe ser no negativo")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

