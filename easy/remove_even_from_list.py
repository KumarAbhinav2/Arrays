"""Implement a function which removes all the even elements from a given list. Name it removeEven(list).
Input - myList = [1,2,4,5,10,6,3]
Output - myList = [1,5,3]
"""

# Mytake

def removeEven(list):
    """
    :param list:
    :return: list
    """
    return [i for i in list if i%2 != 0]


import unittest


class TestRemoveEven(unittest.TestCase):

    def test_success(self):
        mylist = [1, 2, 4, 5, 10, 6, 3]
        actual_output = [1, 5, 3]
        result = removeEven(mylist)
        self.assertEqual(result, actual_output)


if __name__ == '__main__':
    unittest.main()