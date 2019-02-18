

fibonacci_dict = {
    0: 0,
    1: 1,
    2: 1

}


def fibonacci(member_order):
    """ Computes n-th fibonacci number

        Arguments:
        member_order -- n-th

        Returns:
        n-th fibonacci number
    """
    if member_order in fibonacci_dict:
        return fibonacci_dict[member_order]
    else:
        fibonacci_dict[member_order] = fibonacci(member_order - 1) + fibonacci(member_order - 2)
        return fibonacci_dict[member_order]


if __name__ == "__main__":
    print(fibonacci(6))

    print(fibonacci_dict)
