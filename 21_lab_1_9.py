import sys


def flatten(nested_list):
    """ user's function flatten nested list
        Arguments:
        nested_list -- nested list

        Returns: flattened list
    """
    try:
        flattened_list = [element for element in subflatten(nested_list)]
        return flattened_list
    except RecursionError as error:
        print("ValueError: {0}".format(error))
        return nested_list


def subflatten(nested_list):
    """ technical function to flatten nested list
        Arguments:
        nested_list -- nested list
        Returns: flattened list
    """
    try:
        for index in range(len(nested_list)):
            for element in subflatten(nested_list[index]):
                yield element
    except TypeError:
        yield nested_list


def task(nested_list):
    """"""
    return flatten(nested_list)


if __name__ == "__main__":
    a = [1, 1]
    a[1] = a
    print(a)
    print(task(a))

    nested_list_test = [([1, (2), 3], (4, 5), [[6], (7, 8)], 9)]
    print(nested_list_test)
    print(task(nested_list_test))
    
    # let input from command line
    if len(sys.argv) >= 2:
        nested = eval(sys.argv[1])
    else:
        nested = eval(input("Input nested: "))
    print(task(nested))

    """
    nested_list_test = [([1, (2), 3], (4, 5), [[6], (7, 8)], 9)]
    print(nested_list_test)
    print(task(nested_list_test))

    a = [1, 1]
    a[1] = a
    print(a)
    print(task(a))
    """
