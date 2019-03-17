import sys


def get_fibonacci(current_order, answer, next):
    """
    compute fibonacci using tail recursion
    :param current_order: iterator
    :param answer:
    :param next:
    :return:
    """
    if current_order == 0:
        return answer
    return get_fibonacci(current_order - 1, next, answer + next)


def fibonacci_tail_recursion(member_order):
    """ Computes n-th fibonacci number
        Arguments:
        member_order -- order
        Returns:
        n-th fibonacci number
    """

    return get_fibonacci(member_order, 0, 1)


# iterations
def fibonacci_iteration(member_order):
    """
    Computes n-th fibonacci number
    :param member_order:
    :return: n-th fibonacci
    """
    index = 0
    answer = 0
    following = 1
    while index < member_order:
        answer, following = following, answer + following
        index += 1
    return answer


def task(member_order):
    """
    Call fibonacci_iteration function
    :param member_order:
    """
    return fibonacci_iteration(member_order)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        fibonacci_order = int(sys.argv[1])
    else:
        fibonacci_order = int(input("Input fibonacci order "))

    # print(fibonacci_tail_recursion(fibonacci_order))
    print(task(fibonacci_order))
