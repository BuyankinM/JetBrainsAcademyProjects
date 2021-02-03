def check_integer(num):
    if 45 <= num <= 67:
        return num
    raise NotInBoundsError


def error_handling(num):
    try:
        res = check_integer(num)
    except NotInBoundsError as err:
        print(err)
    else:
        print(res)
