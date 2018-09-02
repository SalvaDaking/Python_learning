def insert_star_between_pairs(a_string):

    if a_string == None:
        return None

    new_string = a_string[0]

    for first, second in zip(a_string, a_string[1:]):
        if second == first:
            new_string += "*" + second
        else:
            new_string += second

    return new_string
