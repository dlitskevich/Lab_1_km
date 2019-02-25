import sys

fibonacci_dict = {
    0: 0,
    1: 1

}


def fibonacci(member_order):
    """ Computes n-th fibonacci number

        Arguments:
        member_order -- order

        Returns:
        n-th fibonacci number
    """
    if member_order in fibonacci_dict:
        return fibonacci_dict[member_order]
    else:
        fibonacci_dict[member_order] = fibonacci(member_order - 1) + fibonacci(member_order - 2)
        return fibonacci_dict[member_order]


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        fibonacci_order = int(sys.argv[1])
    else:
        fibonacci_order = int(input("Input fibonacci order "))

    print(fibonacci(fibonacci_order))
    print(fibonacci_dict)
