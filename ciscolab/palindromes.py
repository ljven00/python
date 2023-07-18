
def is_palindrome(string: str):
    """returns True if string is palindrome"""
    new_string = string.lower().replace(" ", "")
    for i in range(len(new_string)):
        if new_string[i] != new_string[~i]:
            return False
    return True

# print(is_palindrome("ana"))