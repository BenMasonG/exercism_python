def distance(strand_a, strand_b):
    '''
    This function compares two strings of equal length and calulates the number
    of differences between the two strings.
    '''
    hamming_distance = 0
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')
    for index, letter in enumerate(strand_a):
        if letter != strand_b[index]:
            hamming_distance += 1
    return hamming_distance
