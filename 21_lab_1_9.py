# import sys


def flatten(nested_list):
    """ user's function flatten nested list
        Arguments:
        nested_list -- nested list

        Returns: flattened list
    """
    flattened_list = [element for element in subflatten(nested_list)]

    return flattened_list


def subflatten(nested_list):
    """ technical function to flatten nested list
        Arguments:
        nested_list -- nested list
        flattened_list -- list to save flattened list
        Returns: flattened list
    """
    if isinstance(nested_list, list):
        for index in range(len(nested_list)):
            for el in subflatten(nested_list[index]):
                yield el
    else:
        yield nested_list


def task(nested_list):
    """"""
    return flatten([nested_list])


if __name__ == "__main__":
    # let input from command line
    """
    if len(sys.argv) >= 2:
        number = int(sys.argv[1])
    else:
        number = int(input("Input number: "))
    """

    nested_list_test = [[1, 2, 3], [4, 5], [6, [7, 8]]]
    print(nested_list_test)
    print(task(nested_list_test))
