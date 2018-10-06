

def get_min(a, b):
    """
        return min number among a and b
    """
    return a if a < b else b


def get_min_without_arguments():
    """
        raise TypeError exception with message
    """
    raise TypeError('you must have at least 1 argument')


def get_min_with_one_argument(x):
    """
        return that value
    """
    return x

def get_min_with_many_arguments(*args):
    """
        return smallest number among args
    """
    result = args[0]
    for i in args:
        if i < result:
            result = i

    return result



def get_min_with_one_or_more_arguments(first, *args):
    """
        return smallest number among first + args
    """
    result = first
    for i in args:
        if i < result:
            result = i

    return result


def get_min_bounded(*args, low, high):
    """
        return smallest number among args bounded by low & high
    """
    result = float('inf')
    for i in args:
        if low < i < high and i < result:
            result = i

    return result


def make_min(*, low, high):
    """
        return inner function object which takes at last one argument
        and return smallest number amount it's arguments, but if the
        smallest number is lower than the 'low' which given as required
        argument the inner function has to return it.
    """

    def inner(first, *args):
        result = float('inf')
        for i in (first,) + args :
            if low < i < high and i < result:
                result = i
        return result if result >= low else low


    return inner
