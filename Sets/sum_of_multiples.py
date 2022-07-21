def sum_of_multiples(limit, multiples):
    uniquie_multiples = set()
    for number in multiples:
        i = 0
        while (i * number) < limit:
            if number == 0:
                break
            multiple = number * i
            uniquie_multiples.add(multiple)
            i += 1
    return sum(uniquie_multiples)
