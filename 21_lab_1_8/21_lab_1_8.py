import sys
import getopt
import re


def get_command(command):
    """

    :param command:
    :return: command name and arguments
    """
    name, arguments = "", ""
    try:
        first_whitespace = 0
        for first_whitespace in range(len(command)):
            if command[first_whitespace] == " ":
                break
            first_whitespace += 1

        name, arguments = \
            command[:first_whitespace], command[first_whitespace+1:]

    except TypeError:
        name = command

    return name, arguments


def add(storage, keys):
    """"""
    if keys == "":
        return storage
    try:
        keys = eval(keys)
    except NameError:
        pass

    if isinstance(keys, list):
        storage.update(keys)
    else:
        storage.add(str(keys))
    return storage


def remove(storage, key):
    """"""
    if key == "":
        return storage
    try:
        key = eval(key)
    except NameError:
        pass
    storage.discard(key)
    return storage


def find(storage, keys):
    """"""
    if keys == "":
        return storage
    try:
        keys = eval(keys)
    except NameError:
        pass

    if isinstance(keys, list):
        found = storage.intersection(keys)
    else:
        found = storage.intersection([keys])
    if found:
        print("Found in storage: {}".format(found))
    else:
        print("Nothing Found")
    return storage


def list_items(storage):
    """"""
    if not storage:
        print("Storage is empty ")
        return storage
    print("Storage: ")
    for item in storage:
        print("  {}".format(item))
    return storage


def grep(storage, regex):
    """"""

    try:
        regex = str(eval(regex))
    except NameError:
        return storage
    found = set()
    for item in storage:
        if re.search(regex, str(item)):
            found.add(item)

    if found:
        print("Matched in storage: {}".format(found))
    else:
        print("Nothing Matched")
    return storage


def save(storage, output):
    """"""
    with open(output, "w") as out:
        for item in storage:
            out.write("{}\n".format(item))
    print("Saved to {}".format(output))
    return storage


def load(input_file):
    """"""
    new_storage = set()
    with open(input_file, "r") as infile:
        for item in infile:
            new_storage.add(item.replace('\n', ''))
    print("Copied from {}".format(input_file))
    return new_storage


def apply_command(input_file, output_file, storage, name="", arguments=""):
    """"""
    print(storage, name, arguments, input_file, output_file)
    commands = {
        "add": "add(storage, arguments)",
        "remove": "remove(storage, arguments)",
        "find": "find(storage, arguments)",
        "list": "list_items(storage)",
        "grep": "grep(storage, arguments)",
        "load": "load(inputfile)",
        "save": "save(storage, outputfile)",
        "exit": "exit(0)"

    }
    if name == "help":
        for pair in commands.items():
            print(pair)
    if name in commands:
        storage = eval(commands[name])
    return storage


def task(in_file, out_file):
    """"""
    storage = set()

    while True:
        command = input(">> ")

        storage = apply_command(in_file, out_file, storage, * get_command(command))


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

    if not outputfile:
        outputfile = "save.txt"
    print(" Output file is ", outputfile)

    if not inputfile:
        inputfile = "load.txt"
    print(" Input file is ", inputfile)

    task(inputfile, outputfile)
