
def add_index(seq):
    yield from enumerate(seq, start=1)

lt = [33, 45, 65]
generator = add_index(lt)

print(next(generator))
print(next(generator))