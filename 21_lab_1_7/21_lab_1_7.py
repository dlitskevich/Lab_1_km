import sys
import getopt
import random


def get_text_stats(file):
    """
    find some stats of text
    :return: text stats
    """

    with open(file, "w") as output:
        """
        quite many chars
        for i in range(1000):
            output.write("{}".format(i) + ": " + chr(i) + "\n")
        """


    print(" Rows: {0} \n"
          " Quantity of words: {1} \n"
          " length of every word: {2}")


def task(file, *arguments):
    """"""
    get_text_stats(file)


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
