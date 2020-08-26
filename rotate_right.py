"""
Implement a function rightRotate(lst,n) which will rotate the given list by k
Input - lst = [1,2,3,4,5]
        n = 3

Output - [3,4,5,1,2]
"""



# step1: last_value = lst[-1]
# step2: lst = lst[:-1]
# step3: lst.insert(0, last_value)


# lst[-n:] + lst[:-n]





















import unittest

# Intuitive way
def rightRotate_intuitive(lst, n):
    new_list = []
    for i in lst:
        new_list.append(i)
    for i in range(len(lst)):
        if i+n >= len(lst):
            new_i = (i+n) - len(lst)
        else:
            new_i = i+n
        new_list[new_i] = lst[i]
    return new_list

# Better way
def rightRotate_better(lst, n):
    n = n % len(lst)   # taking module will help us ensuring while indexing n won't go beyond with big numbers
    return lst[-n:] + lst[:-n] # Idea came from negative indexing in python


class TestRightRotate(unittest.TestCase):

    def setUp(self) -> None:
        self.arr1= [1,2,3,4,5]
        self.n1 = 3
        self.actual_output1 = [3,4,5,1,2]

        self.arr2= [1, 2, 3, 4, 5, 6]
        self.n2 = 2
        self.actual_output2 = [5, 6, 1, 2, 3, 4]

    def test_rightRotate_intuitive(self):
        result = rightRotate_intuitive(self.arr1, self.n1)
        self.assertEqual(result, self.actual_output1)

    def test_rightRotate_better(self):
        result = rightRotate_better(self.arr1, self.n1)
        self.assertEqual(result, self.actual_output1)

        result = rightRotate_better(self.arr2, self.n2)
        self.assertEqual(result, self.actual_output2)


if __name__ == '__main__':
    unittest.main()