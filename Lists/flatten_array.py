def flatten(iterable):
    new_array = []
    for item in iterable:
        if type(item) == list:
            new_array.extend(flatten(item))
        elif type(item) == int:
            new_array.append(item)

    return new_array
