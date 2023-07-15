"""
program that behaves like python
built in split function
"""

def mysplit(s: str, sep = " "):
    """
    splits a given string
    :param s: string to split
    :param sep: separator
    :return: list of separated word
    """
    string_list = []
    if sep not in s:
        string_list.append(s)
    else:
        i = 0
        start = 0
        max = len(s)
        while i < max:
            temp = s.find(sep, i)
            if temp != -1:
                sub = s[start:temp]
                string_list.append(sub)
                i = temp + 1
            else:
                continue
    return string_list

print(mysplit("I love you"))