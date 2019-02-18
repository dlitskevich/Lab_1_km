

def unique_words(sentence):
    """
    Find unique words in a sentence (separated by spaces)
    :param sentence:
    :return: list of unique words (lowercased)
    """
    words_list = sentence.lower().split()
    unique_list = list(set(words_list))
    return unique_list


def even_pairs(sentence):
    """
    clued pairs of words  if their length is even
    :param sentence:
    :return: list of pairs
    """
    pairs = []
    unique_list = unique_words(sentence)
    next_word_index = 0

    for word in unique_list:

        for next_word in unique_list[next_word_index:]:
            new_combination = word + next_word
            if len(new_combination) % 2 == 0:
                pairs.append(new_combination)
        next_word_index += 1

    return pairs


if __name__ == "__main__":
    txt = "A B C A"

    print(unique_words(txt)[1:])
    print(even_pairs(txt))
