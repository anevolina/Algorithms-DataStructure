"""Write a method to return all subsets of a set.
"""

def generate_subsets(given_set):

    if len(given_set) == 0:
        return [[]]

    new_sub_set = given_set[:-1]

    return generate_subsets(new_sub_set) + gen_sub(generate_subsets(new_sub_set), given_set[-1])


def gen_sub(set, value):

    for element in set:
        element.append(value)

    return set

sets = [1, 2, 3, 4]

print(generate_subsets(sets))