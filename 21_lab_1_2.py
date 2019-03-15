

def unique_words(sentence):
    """
    Find unique words in a sentence (separated by spaces)
    :param sentence:
    :return: list of unique words (lowercase)
    """
    words_list = sentence.lower().split()
    unique_list = list(set(words_list))
    return unique_list


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
        combinations_list.append([])
        # to all elements add new word and place it in suitable position
        for row_old in range(row, 0, -1):
            for each_old in range(len(combinations_list[row_old-1])):
                combinations_list[row_old].append(
                    combinations_list[row_old-1][each_old] + new_word
                )
        combinations_list[0].append(new_word)
        # to see how it works step by step
        # print(combinations_list)
        """
        for word_2 in words[i:]:
            combinations_list.append(word_1 + word_2)
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


if __name__ == "__main__":
    txt = "A B C A D A"

    print(unique_words(txt))
    # print(combinations(unique_words(txt)))
    print(even_combinations(unique_words(txt)))

    # print(combinations(["A", "B", "C", "D", "E"]))
    # print(even_combinations(["A", "B", "C", "D", "E"]))
