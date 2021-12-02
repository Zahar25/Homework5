#Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
def my_range(start, stop, step):
    while (start<stop):
        yield start
        start += step

def main():
    generator = my_range(0,20,2)
    try:
        while True:
            print(next(generator))
    except StopIteration:
        StopIteration
if __name__ == '__main__':
    main()