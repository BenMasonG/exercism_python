def square_of_sum(number):
    numbers = list()
    i = 0
    while i <= number:
        numbers.append(i)
        i +=1
    return pow(sum(numbers),2)

def sum_of_squares(number):
    numbers = list()
    i = 0
    while i <= number:
        numbers.append(i)
        i +=1
    for index, number in enumerate(numbers):
        numbers[index] = number ** 2
    return numbers

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
