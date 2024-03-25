def decorator(func):
    def wrapper(x):
        print(func(x))
    return wrapper

@decorator
def decorated(x):
    return x**0.5

decorated(16)