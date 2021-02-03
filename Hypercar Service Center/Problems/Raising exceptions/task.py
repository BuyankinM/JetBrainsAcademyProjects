class NegativeSumError(Exception):
    pass


def sum_with_exceptions(a, b):
    res = a + b
    if res < 0:
        raise NegativeSumError
    return res
