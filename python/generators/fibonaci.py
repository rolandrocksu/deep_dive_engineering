
def get_fibonacci_next():
    first = 1
    second = 1
    while True:
        answer = first + second
        yield answer
        first = second
        second = answer

generator = get_fibonacci_next()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

