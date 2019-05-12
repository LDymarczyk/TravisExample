##Travis example file

def add(a, b):
    """Returns sum of two integers"""
    if type(a) is not int or type(b) is not int:
        return "Bad inputs"
    return a + b

