import sys
import getopt
import random


def merge_sort(*args):
    """"""
    return None
def task(file, *arguments):
    """"""
    if file:
        merge_sort(file, *arguments[:3])
    else:
        print(merge_sort(file, *arguments[:3]))


if __name__ == "__main__":

    argv = sys.argv[1:]
    outputfile = ""

    try:
        opts, args = getopt.getopt(argv, "ho:", ["ofile="])
    except getopt.GetoptError:
        print('21_lab_1_5.py -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('21_lab_1_5.py -o <outputfile>')
            sys.exit()
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if outputfile:
        print(" Output file is ", outputfile)
    else:
        print(" Output in console: \n")

    task(outputfile, *args[:3])
