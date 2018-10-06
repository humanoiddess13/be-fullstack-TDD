def get_max(a, b):
    return a if a > b else b


def get_max_without_arguments():
    raise TypeError('you must have at least one argument')


def get_max_with_one_argument(a):
    return a


def get_max_with_many_arguments(*args):
    result = args[0]
    for i in args:
        if i>result:
            result=i

    return result        


def get_max_with_one_or_more_arguments(first, *args):
    pass


def get_max_bounded(*args, low, high):
    pass


def make_max(*, low, high):
    def inner(first, *args):
        pass

    return inner
