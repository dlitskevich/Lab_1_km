import json
# for test only


def key_to_json(key):
    """"""
    if type(key) == str:
        return object_to_json(key)
    return '\"{}\"'.format(object_to_json(key))


def dict_to_json(dict_py):
    """"""
    valid_keys = [str, int, float, bool]
    object_json = "{"
    for key, value in dict_py.items():
        if not (key is None or type(key) in valid_keys):
            raise ValueError

        object_json += "{0}: {1}".format(key_to_json(key), object_to_json(value))
        # get rid of extra comma
        if key is not list(dict_py.keys())[-1]:
            object_json += ", "

    object_json += "}"
    return object_json


def list_to_json(list_py):
    """"""
    array_json = "["
    for item in list_py:
        array_json += "{}".format(object_to_json(item))
        if item is not list_py[-1]:
            array_json += ", "

    array_json += "]"
    return array_json


def true_or_false(object_py):
    """"""
    if object_py:
        return "true"
    return "false"


def object_to_json(object_py):
    """"""
    types = {
        dict: "dict_to_json(object_py)",
        list: "list_to_json(object_py)",
        tuple: "list_to_json(object_py)",
        str: "'\"{}\"'.format(object_py)",
        int: "object_py",
        float: "object_py",
        bool: "true_or_false(object_py)"

    }
    if object_py is None:
        return "null"

    object_type = type(object_py)
    if object_type in types:
        object_json = eval(types[object_type])
        return object_json
    else:
        raise ValueError


def task(object_py):
    """"""
    return object_to_json(object_py)


if __name__ == "__main__":
    test_object = {
        3: 3,
        "age": 30,
        4: True,
        "divorced": False,
        None: (),
        's': None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
        ]
    }

    # Tests and comparison
    print(task([1.2, 'bye', None, (2, 4, "hello", [True, False])]))
    print(task(test_object))
    print(json.dumps(test_object))

    another_test = {
            "glossary": {
                "title": "example glossary",
                "GlossDiv": {
                    "title": "S",
                    "GlossList": {
                        "GlossEntry": {
                            "ID": "SGML",
                            "SortAs": "SGML",
                            "GlossTerm": "Standard Generalized Markup Language",
                            "Acronym": "SGML",
                            "Abbrev": "ISO 8879:1986",
                            "GlossDef": {
                                "para": "A meta-markup language, used to create markup languages such as DocBook.",
                                "GlossSeeAlso": ["GML", "XML"]
                            },
                            "GlossSee": "markup"
                        }
                    }
                }
            }
        }
    print(task(another_test))
    print(json.dumps(another_test))
