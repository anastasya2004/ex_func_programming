import functools
from datetime import datetime

def logger(func):
    @functools.wraps(func)
    def wrapped(*args):
        try:
            return func(*args)
        except Exception as e:
            with open('log.txt', 'a') as f:
                print(datetime.now(), e, file=f)
    return wrapped

@logger
def div(a, b):
    return a / b

print(div(10, '1'))
