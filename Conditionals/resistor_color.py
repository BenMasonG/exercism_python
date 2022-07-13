def color_code(color):
    '''
    Takes a color and returns the resistence value of that color.

    :param color: str - The color you want to know the resistence value of.
    :return: the resistence value of the given color.
    '''
    if color == 'black':
        return 0
    if color == 'brown':
        return 1
    if color ==  'red':
        return 2
    if color ==  'orange':
        return 3
    if color == 'yellow':
        return 4
    if color == 'green':
        return 5
    if color ==  'blue':
        return 6
    if color == 'violet':
        return 7
    if color == 'grey':
        return 8
    if color ==  'white':
        return 9
    return f'{color} is not a valid resistor color.'


def colors():
    '''
    Returns a list of resistor colors.
    '''
    return ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
