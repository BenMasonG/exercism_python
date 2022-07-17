def is_armstrong_number(number):
    pow_of = []
    num_list = [int(a) for a in str(number)]
    rasise_to = len(num_list)

    for num in num_list:
        pow_of.append(pow(num, rasise_to))

    return sum(pow_of) == number
