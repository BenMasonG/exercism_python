'''
Instructions
Given a moment, determine the moment that would be after a gigasecond has
pass. A gigasction is 10^9 seconds.
'''

import datetime

gigasecond = datetime.timedelta(seconds = 10**9)

def add(moment):
    return moment + gigasecond
