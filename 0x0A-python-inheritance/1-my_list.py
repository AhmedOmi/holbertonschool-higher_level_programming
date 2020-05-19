#!/usr/bin/python3
class MyList(list):
    """
    class inherits from list
    """

    def print_sorted(self):
        """
        prints sorted
        """
        print(sorted(self))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt") 