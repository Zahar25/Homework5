#Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
def my_range(start, stop = None, step = 1):
    if start and not stop and step > 0:
        stop = start
        start = 0
    elif step > 0:
        while start < stop:
            yield start
            start += step
    elif step < 0:
        while start > stop:
            yield start
            start += step



for i in my_range(10,0,-1):
    print(i)