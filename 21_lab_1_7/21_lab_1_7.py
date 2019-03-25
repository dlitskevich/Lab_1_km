import sys
import getopt
import os
import subprocess


def get_text_stats(file):
    """
    find some stats of text
    :return: text stats
    """

    with open(file, "r") as text:

        print(text.read())


def task(file,):
    """"""
    get_text_stats(file)


if __name__ == "__main__":

    argv = sys.argv[1:]

    # current_path = os.path.dirname(__file__)
    inputfile = ""

    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print('21_lab_1_6.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('21_lab_1_6.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg

    if not inputfile:
        # os.system('python ../21_lab_1_6/21_lab_1_6.py 3 4')
        subprocess.run(["python", "../21_lab_1_6/21_lab_1_6.py 3 4", ])
        inputfile = "../21_lab_1_6/output.txt"


    print(" Input file is ", inputfile)

    task(inputfile)
