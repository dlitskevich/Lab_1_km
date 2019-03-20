import sys
import getopt


def merge_two(unsorted_list):
    """"""
    length = len(unsorted_list) // 2
    first_part = unsorted_list[:length]
    second_part = unsorted_list[length:]
    if length == 0:
        yield unsorted_list
    else:
        for i in merge_two(first_part):
            yield i
        for el in merge_two(second_part):
            yield el

    # print(first_part, second_part)


def merge_sort(file, unsorted_list):
    """"""
    for step in merge_two(unsorted_list):
        print(step)

    return None


def task(file, unsorted_list):
    """"""
    if file:
        merge_sort(file, unsorted_list)
    else:
        merge_sort(file, unsorted_list)


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

    list = [13, 4, 10, 6, 15, 1, 12, 7, 9, 16, 3, 11, 5, 8, 2, 14]
    task(outputfile, list)
