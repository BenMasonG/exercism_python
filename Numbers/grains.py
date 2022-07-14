def square(number):
    '''
    The function calculates the number of grains of wheat on a specific 
    square of the chesssboard given that the number of grain on each 
    square doubles.

    :param number: int - the square to calculate how much grain is on it.
    :return: int - the amount of grain on the given square.
    '''
    on_square = 1
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')
    for n in range (1, number):
        on_square *= 2
    return on_square

def total():
    '''
    The function calculates the number of grains of wheat on a chesssboard
    given that the number of grain on each square doubles.
    '''
    on_square = 1
    total = []
    for n in range (1, 65):
        total.append(on_square)
        on_square *= 2
    return sum(total)
