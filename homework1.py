#1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль). Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
class LoginException(Exception):
    pass

def func (username, password, silent=False):
    user_info = [
        {'Vasya': '1214314'}, 
        {'Kolya': 'wasd2001'}, 
        {'Lera': '15751'}, 
        {'Zahar': '080502z'}, 
        {'Artur': '21212sus'}]
    for user in user_info:
        for name, pas in user.items():
            if username == name and password == pas:
                return True
            elif silent:
                return False
    raise LoginException ("Uncorrect password")
print(func(username = 'Lera' , password = '15753', silent = False))