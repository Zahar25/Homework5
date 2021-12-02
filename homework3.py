#На основі попередньої функції створити наступний кусок кода:
# а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
# б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення
def valid (name, password):
    if len(name) < 3:
        raise Exception ('Name shorter than 3')
    if len(name)>50:
        raise Exception('More than 50')
    if len(password) < 8:
        raise Exception ('password length shorter than 8')
    else:
        number = False

        for obj in password:
            if obj.isdigit():
                number = True
                break
        if number is False:
            raise Exception ('password has no digits')
    if len(password) > 20:
        raise Exception ('More than 20 symbols')

list = [('V', '121431467q'), 
        ('Kolya' * 50 , 'wasd20001'), 
        ('Lera', '15751'), 
        ('Zahar', 'Zebrarar5'), 
        ('Artur', 'qwertyasdf'),
        ('Anton', '123' * 20)
        ]
for tuple in list:
    status = ''
    try:
        valid(tuple[0], tuple[1])
        status = 'OK'  
    except Exception as err:
        status = err   
    print(f'Name: {tuple[0]} \nPassword: {tuple[1]} \nStatus: {status}')
    print()