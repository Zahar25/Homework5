#2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#- ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#- пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#- щось своє :)
def valid (name, password):
    if len(name) < 3:
        raise Exception ('Short name')
    if len(name)>50:
        raise Exception('Too big name')
    if len(password) < 8:
        raise Exception ('Short password')
    else:
        number = False

        for obj in password:
            if obj.isdigit():
                number = True
                break
        if number is False:
            raise Exception ('No digits')
    if len(password) > 20:
        raise Exception ('More than 20 symbols')