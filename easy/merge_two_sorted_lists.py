"""
Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list.

Input - list1 = [1,3,4,5]
        list2 = [2,6,7,8]
Output - list3 = [1,2,3,4,5,6,7,8]
"""

# Intuitive way

def merge_lists_intuitive(list1, list2):
    l1_index = 0
    l2_index = 0
    out_index = 0
    out = []
    for i in range(len(list1)+len(list2)):
        out.append(i)
    while (l1_index < len(list1)) and (l2_index < len(list2)):
        if list1[l1_index] < list2[l2_index]:
            out[out_index] = list1[l1_index]
            l1_index +=1
            out_index +=1
        else:
            out[out_index] = list2[l2_index]
            l2_index +=1
            out_index +=1
    # what if lists are not of equal length
    while l1_index < len(list1):
        out[out_index] = list1[l1_index]
        l1_index += 1
        out_index += 1
    while l2_index < len(list2):
        out[out_index] = list2[l2_index]
        l2_index += 1
        out_index += 1
    return out


# Better way

def merge_lists_better(list1, list2):
    l1_index = 0
    l2_index = 0
    while (l1_index < len(list1)) and (l2_index < len(list2)):
        if list1[l1_index] < list2[l2_index]:
            l1_index += 1
        else:
            list1.insert(l1_index, list2[l2_index])
            l2_index += 1
            l1_index += 1
    if l2_index < len(list2):
        list1.extend(list2[l2_index:])
    return list1



import unittest


class TestMergeList(unittest.TestCase):

    def setUp(self) -> None:
        self.list1 = [1,3,4,5]
        self.list2 = [2,6,7,8]
        self.actual_output = [1,2,3,4,5,6,7,8]

    def test_success(self):
        result = merge_lists_intuitive(self.list1, self.list2)
        self.assertEqual(result, self.actual_output)

    def test_success(self):
        result = merge_lists_better(self.list1, self.list2)
        self.assertEqual(result, self.actual_output)


if __name__ == '__main__':
    unittest.main()
