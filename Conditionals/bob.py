def response(hey_bob2):
    '''
    A module to coplete the Bob exercise on exercism.
    '''
    hey_bob = hey_bob2.strip()
    if not hey_bob:
        return 'Fine. Be that way!'
    if not hey_bob.isupper() and hey_bob[-1] == '?':
        return 'Sure.'
    if hey_bob.isupper() and hey_bob[-1] == '?':
        return 'Calm down, I know what I\'m doing!'
    if hey_bob.isupper():
        return 'Whoa, chill out!'
    return 'Whatever.'
