import sys


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def fibonacci(member_order):
    """ Computes n-th fibonacci number

        Arguments:
        member_order -- order

        Returns:
        n-th fibonacci number
    """

    if member_order in (1, 2):
        return 1
    else:
        return fibonacci(member_order - 1) + fibonacci(member_order - 2)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        fibonacci_order = int(sys.argv[1])
    else:
        fibonacci_order = int(input("Input fibonacci order "))

    print(fibonacci(fibonacci_order))
    print(fibonacci(fibonacci_order))
