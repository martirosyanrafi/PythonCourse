def me_decorator(function):
    def wrapper():
        return function() + ', it’s me!'

    return wrapper


def u_decorator(function):
    def wrapper():
        return '<u>' + function() + '</u>'

    return wrapper


@u_decorator
@me_decorator
def hi():
    return 'Hi'
