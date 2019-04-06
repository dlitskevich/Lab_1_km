import sys


def flatten(nested_list):
    """ user's function flatten nested list
        Arguments:
        nested_list -- nested list

        Returns: flattened list
    """
    global possible_recursion_id
    possible_recursion_id = []
    if is_iterable(nested_list):
        flattened_list = [element for element in subflatten(nested_list)]
        return flattened_list
    else:
        return nested_list


def is_iterable(test_object):
    """
    :param test_object:
    :return: bool
    """
    try:
        iter(test_object)
        return True
    except TypeError:
        return False


def subflatten(nested_list):
    """ technical function to flatten nested list
        Arguments:
        nested_list -- nested list
        Returns: flattened list
    """
    try:
        # catch recursive declaration
        if is_iterable(nested_list):
            element_id = id(nested_list)
            if element_id in possible_recursion_id:
                print(nested_list)
                raise ValueError
            else:
                possible_recursion_id.append(element_id)

        # main algorithm
        for index in range(len(nested_list)):
            for element in subflatten(nested_list[index]):
                yield element
    except TypeError:
        yield nested_list


def task(nested_list):
    """"""
    return flatten(nested_list)


if __name__ == "__main__":

    nested_list_test = [([1, (2), 3], (4, 5), [[6], (7, 8)], 9)]
    print(nested_list_test)
    print(task(nested_list_test))
    
    # let input from command line
    if len(sys.argv) >= 2:
        nested = eval(sys.argv[1])
    else:
        nested = eval(input("Input nested: "))
    print(task(nested))

    # example of recursive list
    a = [1, 1]
    a[1] = a
    b = [1, 2, 3, [4, [5, [6, 7, a]]]]
    print(b)
    print(task(b))
