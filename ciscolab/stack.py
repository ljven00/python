class Stack:

    """
    Implements a real world stack.
    """

    def __init__(self, *args):
        self.__value = list(args) if len(args) > 0 else []
        self.__size = len(self.__value)

    def push(self, val):
        self.__size += 1
        self.__value.append(val)

    def pop(self):
        if self.__size <= 0:
            return None
        self.__size -= 1
        return self.__value.pop()

    def extend(self, *args):
        if len(args) <= 0:
            return
        self.__size += len(*args)
        self.__value.extend(*args)

    def get_size(self):
        return self.__size

    def __str__(self):
        return " ".join([str(item) for item in self.__value])

    def __eq__(self, other):
        return self.__value == other

stack = Stack(0, 1, 2, 3, 4)
stack2 = Stack(0, 1, 2, 3, 4)

