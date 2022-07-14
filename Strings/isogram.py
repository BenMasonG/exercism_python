def is_isogram(string):
    '''
    This function checks it a given string is an isogram.
    '''
    char_list = []
    for char in string.lower():
        if char in char_list:
            return False
        if char.isalpha():
            char_list.append(char)
    return True
