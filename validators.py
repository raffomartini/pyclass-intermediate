'''
Validators for the properties module.
'''


def is_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError('Expected int or float, got {!r}'.format(type(value).__name__))
    return True

def is_positive(value):
    if value < 0:
        raise ValueError('Must be positive')
    return True