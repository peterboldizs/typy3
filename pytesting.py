__author__ = 'fnxuser'
import doctest


def avg(values):
    """
    >>> print(avg([20,30,70]))
    40.0
    """
    return sum(values) / len(values)


doctest.testmod()
