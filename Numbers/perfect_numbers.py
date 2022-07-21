def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')
    
    sum_of_factors = list()
    i = 1

    while i < number:
        i += 1
        if number % i == 0:
            sum_of_factors.append(int(number / i))

    if sum(sum_of_factors) == number:
        return 'perfect'
    if sum(sum_of_factors) > number:
        return 'abundant'
    if sum(sum_of_factors) < number:
        return 'deficient'
