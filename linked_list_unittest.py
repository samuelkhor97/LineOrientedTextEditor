"""
@author: Khor Peak Siew
@since: 14/9/2018
@modified: 14/9/2018
"""

import unittest
from linked_list import linkedList


class MyTest(unittest.TestCase):

    def test_is_empty_true(self):
        my_list = linkedList()
        self.assertTrue(my_list.is_empty())

    def test_is_empty_false(self):
        my_list = linkedList()
        my_list.append(1)
        self.assertFalse(my_list.is_empty())

    def test_reset_list(self):
        my_list = linkedList()
        my_list.append(1)
        my_list.reset()
        self.assertTrue(my_list.is_empty())

    def test_append_empty_list(self):
        my_list = linkedList()
        my_list.append(2)
        self.assertEqual(my_list[0].value, 2)

    def test_insert_valid_index_empty_list(self):
        my_list = linkedList()
        self.assertTrue(my_list.insert(0, 1))

    def test_insert_invalid_index_empty_list(self):
        my_list = linkedList()
        self.assertFalse(my_list.insert(1, 1))

    def test_insert_valid_index_full_list(self):
        my_list = linkedList()
        my_list.append(1)
        self.assertTrue(my_list.insert(1, 2))

    def test_remove_valid_item(self):
        my_list = linkedList()
        my_list.append("remove this")
        self.assertTrue(my_list.remove("remove this"))

    def test_remove_invalid_item(self):
        my_list = linkedList()
        my_list.append(1)
        self.assertFalse(my_list.remove("remove this"))

    def test_delete_at_valid_index(self):
        my_list = linkedList()
        for i in range(10):
            my_list.append(i)
        self.assertTrue(my_list.delete(1))

    def test_delete_at_invalid_index(self):
        my_list = linkedList()
        for i in range(10):
            my_list.append(i)
        self.assertFalse(my_list.delete(-11))

    def test_sort_reversed(self):
        my_list = linkedList()
        for i in range(20):
            my_list.append(i)

        comparison_list = linkedList()
        for i in range(19, -1, -1):
            comparison_list.append(i)

        my_list.sort(True)
        self.assertEqual(my_list, comparison_list)

    def test_sort_not_reversed(self):
        my_list = linkedList()
        for i in range(19, -1, -1):
            my_list.append(i)

        comparison_list = linkedList()
        for i in range(20):
            comparison_list.append(i)

        my_list.sort(False)
        self.assertEqual(my_list, comparison_list)

if __name__ == '__main__':
    unittest.main()
