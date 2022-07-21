def convert(number):
    result = ''
    if number % 3 == 0:
         result += 'Pling'
    if number % 5 == 0:
        result += 'Plang'
    if number % 7 == 0:
        result += 'Plong'
    if len(result) > 1:
        return result
    return str(number)
