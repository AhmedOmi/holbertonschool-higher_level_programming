##!/usr/bin/python
'''
text_indentation
'''


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for string in ".?:":
        text = (string + "\n\n").join(
            [i.strip(" ")for i in text.split(string)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
