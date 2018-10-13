def get_max(a, b):
    """

    Returns max number among a and b.
    """
    return a if a > b else b


def get_max_without_arguments():
    """

    Raises TypeError exception with message.
    """
    raise TypeError('you must have at least one argument')


def get_max_with_one_argument(a):
    """

    Return that value.
    """
    return a


def get_max_with_many_arguments(*args):
    """
    Return max number among numbers of args.
    """
    max_number = None
    for i in args:
        max_number = i if max_number is None or i > max_number else max_number

    return max_number


def get_max_with_one_or_more_arguments(first, *args):
    """

    Return max number among numbers of args + first.
    """
    max_number = None
    for i in (first,) + args:
        max_number = i if max_number is None or i > max_number else max_number

    return max_number


def get_max_bounded(*args, low, high):
    """

    Return max number among numbers of args bounded by low and high.
    """
    max_number = None
    for i in args:
        max_number = i if low < i < high and (max_number is None or i > max_number) else max_number

    return max_number


def make_max(*, low, high):
    """

    Return inner function object which returns max number among args + first, but if the
        max number is higher than the 'high' which given as required
        argument the inner function has to return it.
    """
    def inner(first, *args):
        max_number = None
        for i in (first,) + args:
            max_number = i if low < i < high and (max_number is None or i > max_number) else max_number
        return max_number if max_number <= high else high

    return inner
