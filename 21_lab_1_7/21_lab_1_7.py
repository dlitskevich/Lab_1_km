import sys
import getopt
import os
import nltk.tokenize
from collections import defaultdict


def sentence_to_words(sentence):
    """"""
    punktuation = ",.:;!?"
    words = nltk.tokenize.word_tokenize(sentence)

    for word in words:
        for punkt in punktuation:
            if word == punkt:
                words.remove(word)
    return words


def textfile_to_swords(file_to_read):
    """"""
    text = file_to_read.read().replace("\n", " ").lower()
    sentences = nltk.tokenize.sent_tokenize(text)

    for index in range(len(sentences)):
        sentences[index] = sentence_to_words(sentences[index])
    return sentences


def count_words(text):
    """"""
    words_dict = defaultdict(int)  # default value of int is 0
    for sentence in text:
        for word in sentence:
            words_dict[word] += 1

    return words_dict


def average_quantity(text):
    """"""
    total_quantity_words = 0
    quantity_sentences = len(text)
    for sentence in text:
        total_quantity_words += len(sentence)

    average = total_quantity_words / quantity_sentences
    return average


def median_quantity(text):
    """"""
    quantity_words = []
    median_index = len(text) // 2 - 1

    for sentence in text:
        quantity_words.append(len(sentence))

    median = sorted(quantity_words)[median_index]
    return median


def grams(text, gram_length):
    """"""
    top_gram = defaultdict(int)
    for sentence in text:
        for word in sentence:
            if len(word) >= gram_length:
                for start_position in range(len(word)-gram_length+1):
                    new_gram = word[start_position:start_position+gram_length]
                    top_gram[new_gram] += 1

    print(top_gram)
    return top_gram


def top_grams(text, top_capacity, length):
    """"""
    all_grams = grams(text, length)
    top_only_grams = defaultdict(int)
    # TODO: detect largest values and save their keys
def get_text_stats(file, top_number, number_grams):
    """
    find some stats of text
    :return: text stats
    """
    file_stats = os.stat(file)
    file_size = file_stats.st_size

    # file size MUST be less than 1mb
    assert file_size < 2**20, "\n File too large! \n"

    with open(file, "r") as text_file:
        text = textfile_to_swords(text_file)

        print("Quantity of every word: \n")
        for word, quantity in count_words(text).items():
            print("  {0}: {1}".format(word, quantity))

        print("\nAverage quantity of words in sentences:"
              " {}".format(int(average_quantity(text))))

        print("\nMedian quantity of words in sentences:"
              " {}\n".format(median_quantity(text)))
        grams(text, top_number, number_grams)


def task(file, top_length, length_gram):
    """"""
    if not isinstance(top_length, int):
        top_length = 10
    if not isinstance(length_gram, int):
        length_gram = 4

    get_text_stats(file, top_length, length_gram)


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
        task(inputfile, * sys.argv[2:])
    # Input from keyboard
    else:
        inputfile = input("Inputfile path: ")
        top_quantity = input("Input length of Top n-grams: ")
        length_n_gram = input("Input length of n-grams: ")
    # for test purposes MUST exist garbage_generator
    if not inputfile:
        generate_new = input("Wanna generate new file? ")
        if generate_new:
            os.system('python ../21_lab_1_6/21_lab_1_6.py -o garbage.txt 40 60 3')
        # TODO: change to garbage.txt
        inputfile = "text.txt"

    print("\n Input file is {} \n".format(inputfile))
    # if needed
    # nltk.download('punkt')

    task(inputfile, top_quantity, length_n_gram)
