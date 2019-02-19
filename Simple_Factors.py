import math as mth


def simple_factors(composite_number):
    """

    :param composite_number:
    :return: list of prime factors (sorted)
    """
    factors = []
    number = composite_number
    while number >= 2:
        factor = one_factor(number)
        factors.append(factor)
        number //= factor

    return factors


def one_factor(composite_number):
    """
    Compute the smallest factor of the given number
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
    print(simple_factors(4*19*37*9))
