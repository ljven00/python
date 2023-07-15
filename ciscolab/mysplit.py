"""
program that behaves like python
built in split function
"""

def mysplit(string: str, sep = " "):
    """
    splits a given string
    :param s: string to split
    :param sep: separator
    :return: list of separated word
    """
    word = ""
    string_list = []
    if string.isspace():
        return []
    for c in string:
        if c == sep:
            string_list.append(word)
            word = ""
            continue
        word += c
    string_list.append(word)
    return string_list


print(mysplit("I love you"))