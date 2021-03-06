class Node:

    def __init__(self, word, level, parent):
        self.word = word
        self.level = level
        self.parent = parent


class Path:

    def __init__(self, path, n, step):
        self.path = path
        self.n = n
        self.step = step


class Queue:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__elements = []
        self.__size = len(self.__elements)

    def enqueue(self, element):
        if self.is_full():
            raise Exception

        self.__elements.append(element)
        self.__size = len(self.__elements)
        return True

    def dequeue(self):
        if self.is_empty():
            raise Exception

        self.__elements.reverse()
        value = self.__elements.pop()
        self.__elements.reverse()
        self.__size = len(self.__elements)

        return value

    def is_empty(self):
        return True if self.__size == 0 else False

    def is_full(self):
        return True if self.__size == self.__capacity else False
