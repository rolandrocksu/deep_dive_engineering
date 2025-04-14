def filter_odds(seq):
    for i in range(len(seq)):
        if not i%2:
            yield seq[i]

lt = [1, 2, 3, 4, 5, 6, 7, 8]
generator = filter_odds(lt)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))