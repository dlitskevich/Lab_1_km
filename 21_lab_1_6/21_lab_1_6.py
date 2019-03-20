import sys
import getopt
import random


def random_syllable():
    """
    random syllable in range 33 - 126 (can be more)
    :return: char
    """
    return chr(random.randrange(33, 126))


def garbage_word(length):
    """
    create word from random syllables
    :param length:
    :return: word
    """
    word = ""
    for syllable in range(length):
        word += random_syllable()
    return word


def generate_garbage(file, rows, quantity, length=random.randrange(1, 16)):
    """
    fill file with garbage
    :param file: where to write
    :param rows:
    :param quantity: of words in a row
    :param length: of each word
    :return: None
    """
    try:
        rows, quantity, length = \
            int(rows), int(quantity), int(length)
    except ValueError as err:
        print("rows, quantity, length must be positive int: {}".format(err))
        sys.exit(3)
    assert quantity > 0 and rows > 0 and length > 0, \
        "rows, quantity, length must be positive int"

    with open(file, "w") as output:
        """
        quite many chars
        for i in range(1000):
            output.write("{}".format(i) + ": " + chr(i) + "\n")
        """
        for row in range(rows):
            for word in range(quantity):
                output.write(garbage_word(length) + "   ")
            output.write("\n")

    print(" Rows: {0} \n"
          " Quantity of words: {1} \n"
          " length of every word: {2}".format(rows, quantity, length))


def task(file, *args):
    """"""
    generate_garbage(file, *args[:3])


if __name__ == "__main__":

    argv = sys.argv[1:]
    outputfile = "output.txt"

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

    print(" Output file is ", outputfile)

    task(outputfile, *args[:3])
