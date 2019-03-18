import sys
import getopt
import random


def generate_garbage(rows, quantity, length=random.randrange(1, 16)):
    """"""
    try:
        rows, quantity, length = \
            int(rows), int(quantity), int(length)
    except ValueError as err:
        print("rows, quantity, length must be positive int: {}".format(err))
        sys.exit(3)
    assert quantity > 0 and rows > 0 and length > 0, \
        "rows, quantity, length must be positive int"

    print(rows, quantity, length)


if __name__ == "__main__":

    argv = sys.argv[1:]
    outputfile = 'output.txt'

    try:
        opts, args = getopt.getopt(argv, "ho:", ["ofile="])
    except getopt.GetoptError:
        print('21_lab_1_6.py -o <outputfile> rows quantity length')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('21_lab_1_6.py -o <outputfile> rows quantity length')
            sys.exit()
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print('Output file is ', outputfile)

    generate_garbage(*args[:3])
