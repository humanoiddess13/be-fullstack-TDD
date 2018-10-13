

def get_min(a, b):
    """
        Return minimal number among a and b.
    """
    return a if a < b else b


def get_min_without_arguments():
    """
        Raise TypeError exception with message.
    """
    raise TypeError('You must have at least 1 argument.')


def get_min_with_one_argument(x):
    """
        Return that value.
    """
    return x


def get_min_with_many_arguments(*args):
    """
        Return smallest number among numbers in args.
    """
    min_number = None
    for i in args:
        min_number = i if min_number is None or i < min_number else min_number

    return min_number


def get_min_with_one_or_more_arguments(first, *args):
    """
        Return smallest number among first and numbers in args.
    """
    min_number = None
    for i in (first,) + args:
        min_number = i if min_number is None or i < min_number else min_number

    return min_number


def get_min_bounded(*args, low, high):
    """
        Return smallest number among numbers in args bounded by low & high.
    """
    min_number = None
    for i in args:
        min_number = i if low < i < high and (min_number is None or i < min_number) else min_number

    return min_number


def make_min(*, low, high):
    """
        Return inner function object which takes at least one argument
        and return smallest number amount it's arguments, but if the
        smallest number is lower than the 'low' which given as required
        argument the inner function has to return it.
    """

    def inner(first, *args):
        min_number = None
        for i in (first,)+args:
            min_number = i if low < i < high and (min_number is None or i < min_number) else min_number
        return min_number if min_number >= low else low

    return inner
