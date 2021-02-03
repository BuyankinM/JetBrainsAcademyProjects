import math


def my_sqrt(value):
    if type(value) is int or type(value) is float:
         return (math.sqrt(value))
    elif type(value) is str:
         return "The string should be converted into a numeric data type"
    else:
        return None