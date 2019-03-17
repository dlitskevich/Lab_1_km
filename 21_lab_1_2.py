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


def combinations(words, length):
    """
    combine words
    :param words:
    :param length: how many elements in each list
    :return: list of all possible combinations not repeating elements
        of the same length
    """
    quantity = len(words)
    combinations_list = []
    index = list(range(length))
    done = 0
    while True:
        new_word = []
        # print(index)
        for element in index:
            new_word.append(words[element])
        combinations_list.append(new_word)
        # print(new_word)
        new_step = 0
        for number in range(length-1, 0, -1):
            if not new_step:
                index[number] += 1
            element = index[number]
            # print(element)
            # print(quantity - length + number)
            if element > quantity - length + number:
                new_step = 1
                # print(index)
                index[number-1] += 1
                # print(index[0])

                if index[0] > quantity - length:
                    done = 1

                else:
                    index[number-1:] = \
                     range(index[number-1],
                           index[number-1]+length-number+1, 1)
                # print(index)

            if not new_step:
                break
        if done:
            break
    return combinations_list


def even_combinations(words):
    """
    from all combinations return only even
    :param words:
    :return: list of even combinations
    """
    even_combinations_list = []
    for even in range(2, len(words)//2 + 3, 2):
        even_combinations_list.append(combinations(words, even))
    return even_combinations_list


def task(text_to_split):
    """"""
    words = unique_words(text_to_split)
    return even_combinations(words)


if __name__ == "__main__":
    # print(combinations(["A", "B", "C", "D", "E", "F"], 2))

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
