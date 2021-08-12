def check_permission(user):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user in user_permissions:
                func(*args, **kwargs)
            else:
                raise PermissionError(': У пользователя недостаточно прав, чтобы выполнить функцию add_comment')

        return wrapper

    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
