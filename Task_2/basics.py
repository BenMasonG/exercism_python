"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(minutes_baked):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - minutes_baked

def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the prepation time.

    :param number_of_layers: int the number of layers in the lasanga
    :return: int total time preparation will take.

    This function takes an integer showing the number of layers in the lasagna. It then
    multiples this by the constant preparation time of 2 minutes per layer to calculate
    the total preparation time in minutes.
    """

    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the elapsed cooking time.

    :param number_of_layers: int the number of layers in the lasanga
    :param elapsed_bake_time: int the elapsed baking time
    :return: int total time elapsed, in minutes, of preperation and baking

    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return (number_of_layers * PREPARATION_TIME) + elapsed_bake_time
    