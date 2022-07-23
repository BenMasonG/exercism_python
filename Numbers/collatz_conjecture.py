def steps(number):
    """
    _summary_
    When a positive integer is passed the function will count how many steps
    it takes to reach 1 using the formula indicated by Collatz conjecture.
    Even numbers are divded by 2 and odd numbers timesed by 3 then 1 is
    added. This is repeated until the orginal number equals 1.

    Args:
        number (int): any positive integer

    Raises:
        ValueError: if the arg passed is no a positive integer an error
        is thrown

    Returns:
        int: the number of steps it takes for the number to be reduced to 1.
    """

    if number < 1:
        raise ValueError("Only positive integers are allowed")

    number_of_steps = 0

    while number != 1:
        number = 3 * number + 1 if number % 2 else number / 2
        number_of_steps += 1

    return number_of_steps
