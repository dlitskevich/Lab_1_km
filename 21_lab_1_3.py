import sys
import math as mth


def simple_factors(composite_number):
    """
    Form array of prime factors (1 is not prime)
    :param composite_number:
    :return: list of prime factors (sorted)
    """
    factors = []

    # not affecting outer variable
    while composite_number >= 2:
        factor = one_factor(composite_number)
        factors.append(factor)
        composite_number //= factor

    return factors


def one_factor(composite_number):
    """
    Compute the smallest factor of the given composite_number
    :param composite_number:
    :return: primal factor
    """
    if composite_number <= 3:
        return composite_number

    for factor in range(2, 1 + mth.ceil(mth.sqrt(composite_number))):
        if composite_number % factor == 0:
            return factor

    return composite_number


if __name__ == "__main__":
    # let input from command line
    if len(sys.argv) >= 2:
        number = int(sys.argv[1])
    else:
        number = int(input("Input number: "))

    print(simple_factors(number))
    print(number)
