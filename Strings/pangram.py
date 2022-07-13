'''
A module for the exercism exercise Pangram.
'''

PATTERN = ('abcdefghijklmnopqrstvxyz')
alphabet = set(PATTERN)

def is_pangram(sentence):
    '''
    The function takes a string and determines if it is a Pangram.

    :param sentence: str - any string.
    :return: bool - true if sentence is a Pangram. False if not.
    '''
    return set(sentence.lower()) >= alphabet
