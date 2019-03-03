import sys


def get_fibonacci(curent_order, answer, next):
    """
    compute fibonacci using tail recursion
    :param curent_order: iterator
    :param answer:
    :param next:
    :return:
    """
    if curent_order == 0:
        return answer
    return get_fibonacci(curent_order - 1, next, answer + next)


def fibonacci(member_order):
    """ Computes n-th fibonacci number

        Arguments:
        member_order -- order

        Returns:
        n-th fibonacci number
    """

    return get_fibonacci(member_order, 0, 1)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        fibonacci_order = int(sys.argv[1])
    else:
        fibonacci_order = int(input("Input fibonacci order "))

    print(fibonacci(fibonacci_order))
