'''
This module is for the leap exercise on exercism.com.
'''

def leap_year(year):
    '''
    This is a function to determine if a given year is a leap yaer.

    :param year: int - a year.
    :result: Bool - True if the year is a leap year or no if it is not a leap
    year.
    '''
    if  year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
