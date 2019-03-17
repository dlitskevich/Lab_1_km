import sys


def unique_words(sentence):
    """
    Find unique words in a sentence (separated by spaces)
    :param sentence:
    :return: list of unique words (lowercase)
    """
    words_list = sentence.lower().split()
    unique_list = list(set(words_list))
    return unique_list


def add_word_combinations(old_combinations, new_word, order):
    """
    to all elements add new word and place it in suitable position
    :param old_combinations:
    :param new_word:
    :param order:
    :return: list of all combinations with current words
    """
    combinations_list = old_combinations
    combinations_list.append([])

    for row_old in range(order, 0, -1):
        for each_old in range(len(combinations_list[row_old - 1])):
            combinations_list[row_old].append(
                combinations_list[row_old - 1][each_old] + new_word
            )
    combinations_list[0].append(new_word)
    return combinations_list


def combinations(words):
    """
    combine words
    :param words:
    :return: list of all possible combinations not repeating elements
    """
    quantity = len(words)
    combinations_list = []

    for row in range(0, quantity):
        new_word = [words[row]]
        combinations_list = \
            add_word_combinations(combinations_list, new_word, row)
        """
        to see how it works step by step
        print(combinations_list)
        """
    return combinations_list


def even_combinations(words):
    """
    from all combinations return only even
    :param words:
    :return: list of even combinations
    """
    all_combinations = combinations(words)
    even_combinations_list = []
    for even in range(1, len(words)+1//2, 2):
        even_combinations_list.append(all_combinations[even])
    return even_combinations_list


def task(text_to_split):
    """"""
    words = unique_words(text_to_split)
    return even_combinations(words)


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        text = (sys.argv[1])
    else:
        text = (input("Input text: "))

    print(unique_words(text))
    print(task(text))

    """ Testament
    # text = "A B C A D A E"
    # print(combinations(unique_words(txt)))
    # print(combinations(["A", "B", "C", "D", "E"]))
    # print(even_combinations(["A", "B", "C", "D", "E"]))
    """
