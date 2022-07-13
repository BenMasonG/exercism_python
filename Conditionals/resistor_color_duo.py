'''
This module is to complete the color duo exercise on exercism
'''

def value(*colors):
    '''
    This is a function to determine the resistence value by taking the color of the
    first two resisters in a list. e.g. resistor 1 value = 1 and resistor 2 value =
    6 the total resistence value would equal 16.
    
    :param color: list - an unknown number of colors representing resistors.
    :return: int - the total reistence value
    '''

    bands = [0,0]

    if colors[0][0] == 'black':
        bands[0] = 0
    elif colors[0][0] == 'brown':
        bands[0] = 1
    elif colors[0][0] ==  'red':
        bands[0] = 2
    elif colors[0][0] ==  'orange':
        bands[0] = 3
    elif colors[0][0] == 'yellow':
        bands[0] = 4
    elif colors[0][0] == 'green':
        bands[0] = 5
    elif colors[0][0] ==  'blue':
        bands[0] = 6
    elif colors[0][0] == 'violet':
        bands[0] = 7
    elif colors[0][0] == 'grey':
        bands[0] = 8
    elif colors[0][0] ==  'white':
        bands[0] = 9

    if colors[0][1] == 'black':
        bands[1] = 0
    elif colors[0][1] == 'brown':
        bands[1] = 1
    elif colors[0][1] ==  'red':
        bands[1] = 2
    elif colors[0][1] ==  'orange':
        bands[1] = 3
    elif colors[0][1] == 'yellow':
        bands[1] = 4
    elif colors[0][1] == 'green':
        bands[1] = 5
    elif colors[0][1] ==  'blue':
        bands[1] = 6
    elif colors[0][1] == 'violet':
        bands[1] = 7
    elif colors[0][1] == 'grey':
        bands[1] = 8
    elif colors[0][1] ==  'white':
        bands[1] = 9

    resistance_value = f'{bands[0]}{bands[1]}'

    return int(resistance_value)

#An alternate and more efficent way to do the above.
color_dict = {
                'black': 0,
                'brown': 1,
                'red': 2,
                'orange': 3,
                'yellow': 4,
                'green': 5,
                'blue': 6,
                'violet': 7,
                'grey': 8,
                'white': 9
              }
def value2(colors):
    '''
    This is a function to determine the resistence value by taking the color of the
    first two resisters in a list. e.g. resistor 1 value = 1 and resistor 2 value =
    6 the total resistence value would equal 16.
    
    :param color: list - an unknown number of colors representing resistors.
    :return: int - the total reistence value
    '''
    return int(str(color_dict[colors[0]]) + str(color_dict[colors[1]]))
