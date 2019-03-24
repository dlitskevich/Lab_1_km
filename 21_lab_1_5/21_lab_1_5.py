import sys
import getopt
import math


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


def divide_list(plain_list):
    """"""
    length = len(plain_list)
    max_exponent = int(math.log(length, 2))
    for exponent in range(max_exponent-1, 0, -1):
        step = 2
        index_start, index_end = 0, step

        while index_start < 2 ** exponent:
            plain_list[index_start:index_end] = [plain_list[index_start:index_end]]
            index_start, index_end = index_start + 1, index_end + step - 1

    return plain_list



def merge_sort(file, unsorted_list):
    """"""
    divided_list = divide_list(unsorted_list)
    for step in merge_two(unsorted_list):
        print(step)

    return divided_list


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

    list_test = [13, 4, 10, 6, 15, 1, 12, 7, 9, 16, 3, 11, 5, 8, 2, 14]
    task(outputfile, list_test)
    print(divide_list(list_test))
