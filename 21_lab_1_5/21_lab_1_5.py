import sys
import getopt
import math


def merge_two(unsorted_list):
    """"""

    length = len(unsorted_list) // 2
    if length < 1:
        return unsorted_list

    first_part = unsorted_list[:length][0]
    second_part = unsorted_list[length:][0]

    sorted_list = []
    while first_part and second_part:
        if first_part[0] < second_part[0]:
            smaller = first_part.pop(0)
        else:
            smaller = second_part.pop(0)
        sorted_list.append(smaller)
        # print(smaller, sorted_list, first_part, second_part)

    while first_part:
        sorted_list.append(first_part.pop(0))

    while second_part:
        sorted_list.append(second_part.pop(0))
    # print(unsorted_list, sorted_list)
    return sorted_list


def merge_sort(plain_list):
    """"""
    length = len(plain_list)
    max_exponent = int(math.log(length, 2))
    for exponent in range(max_exponent, -1, -1):
        step = 2 if exponent < max_exponent else 1
        index_start, index_end = 0, step

        while index_start < 2 ** exponent:
            plain_list[index_start:index_end] = \
                [merge_two(plain_list[index_start:index_end])]
            index_start, index_end = index_start + 1, index_end + 1
        yield plain_list


def task(file, unsorted_list):
    """"""
    if not file:
        for element in merge_sort(unsorted_list):
            print(element)
    else:
        with open(file, "w") as output:
            for merge_sorted_step in merge_sort(unsorted_list):
                output.write("{0}\n".format(merge_sorted_step))


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
