"""Заданиие 1"""

def uppercase(func):
    def wrapper(words):
        result = func(words)
        if type(result) is str:
            return result.upper()
        return result
    return wrapper

@uppercase
def say (greetings):
    return f'{greetings}'

print (say("привет всем!"))

"""Задание 2"""
def require_admin(func):
    def wrapper(correct_role):
        result = func(correct_role)
        if result == "admin":
            return 'Доступ разрешен!'
        else:
            return 'ДОСТУП ЗАПРЕЩЕН!'
    return wrapper

@require_admin
def enter_role (right_role):
    return f'{right_role}'

print (enter_role("boss"))





