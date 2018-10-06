def get_max(a, b):
    """

    :param a:
    :param b:
    :return max number among a and b:
    """
    return a if a > b else b


def get_max_without_arguments():
    """

    :raises TypeError exception with message:
    """
    raise TypeError('you must have at least one argument')


def get_max_with_one_argument(a):
    """

    :param a:
    :return a:
    """
    return a


def get_max_with_many_arguments(*args):
    """
    :param args:
    :return max number among numbers of args:
    """
    result = args[0]
    for i in args:
        if i>result:
            result=i

    return result


def get_max_with_one_or_more_arguments(first, *args):
    """

    :param first:
    :param args:
    :return max number among numbers of args + first:
    """
    result = -float('inf')
    for i in (first,) + args:
        if i > result:
            result = i

    return result



def get_max_bounded(*args, low, high):
    """

    :param args:
    :param low:
    :param high:
    :return max number among numbers of args bounded by low and high:
    """
    result = -float('inf')
    for i in args:
        if low < i < high and i > result:
            result = i

    return result


def make_max(*, low, high):
    """

    :param low:
    :param high:
    :return inner function object which returns max number among args + first, but if the
        max number is higher than the 'high' which given as required
        argument the inner function has to return it:
    """
    def inner(first, *args):
        result = -float('inf')
        for i in (first,) + args:
            if low < i < high and i > result:
                result = i
        return result if result <= high else high

    return inner
