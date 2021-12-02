def generator(numbers):
    while True:
        for obj in numbers:
            yield obj
gener = {1: 1, 2:4, 3:6}
for n in generator(gener):
    print(n)