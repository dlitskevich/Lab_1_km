import sys
import getopt
import os
import string
import nltk.tokenize

def sentence_to_words(sentence):
    """"""
    punktuation = ",.:;!?"
    words = nltk.tokenize.word_tokenize(sentence)

    for word in words:
        for punkt in punktuation:
            if word == punkt:
                words.remove(word)
    return words

def get_text_stats(file):
    """
    find some stats of text
    :return: text stats
    """

    with open(file, "r") as text_file:
        text = text_file.read().replace("\n", "")
        sentence = nltk.tokenize.sent_tokenize(text)

        for element in sentence:
            this = sentence_to_words(element)



def task(file,):
    """"""
    get_text_stats(file)


if __name__ == "__main__":
    # Console arguments
    if len(sys.argv) > 1:
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
    # Input from keyboard
    else:
        inputfile = input("Inputfile path: ")
    # for test purposes MUST exist garbage_generator
    if not inputfile:
        generate_new = input("Wanna generate new file? ")
        if generate_new:
            os.system('python ../21_lab_1_6/21_lab_1_6.py -o garbage.txt 40 60 3')
        # subprocess.run(["python", "../21_lab_1_6/21_lab_1_6.py 3 4", ])
        inputfile = "text.txt"

    print("\n Input file is {} \n".format(inputfile))
    # if needed
    # nltk.download('punkt')

    task(inputfile)
