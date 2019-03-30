import sys
import getopt
import math


def task(file, unsorted_list):
    """"""
    if not file:
        print()
    else:
        with open(file, "w") as output:
            print()


if __name__ == "__main__":

    argv = sys.argv[1:]
    outputfile = ""
    inputfile = ""

    try:
        opts, args = getopt.getopt(argv, "ho:i:", ["ofile=", "ifile="])
    except getopt.GetoptError:
        print('21_lab_1_5.py -o <outputfile> -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('21_lab_1_5.py -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if outputfile:
        print(" Output file is ", outputfile)
    else:
        print(" Output in console: \n")

    if inputfile:
        print(" Input file is ", inputfile)
        with open(inputfile, "r") as input_file:
            list_merge = input_file.read()
        task(outputfile, eval(list_merge))

    else:
        list_test = [13, 4, 10, 6, 15, 1, 12, 7, 9, 16, 3, 11, 5, 8, 2, 14]
        print("List to Merge_Sort: ", list_test)
        task(outputfile, list_test)
