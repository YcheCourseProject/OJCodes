import random
import unittest


def binary_search_detail(num_list, begin, end, target_val):
    if begin == end:
        return None
    else:
        med_idx = (begin + end) / 2
        if target_val == num_list[med_idx]:
            return med_idx
        elif target_val < num_list[med_idx]:
            return binary_search_detail(num_list, begin, med_idx, target_val)
        else:
            return binary_search_detail(num_list, med_idx + 1, end, target_val)


def binary_search(num_list, target_val):
    return binary_search_detail(num_list, 0, len(num_list), target_val)


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_recursion(self):
        range_num = 100
        my_list = sorted(random.sample(range(0, 100), range_num))
        expected_list = range(range_num)
        res_list = [binary_search(my_list, my_list[i]) for i in range(range_num)]
        self.assertListEqual(res_list, expected_list)

        for num in range(0, 100):
            if num not in set(my_list):
                self.assertTrue(binary_search(my_list, num) is None)


if __name__ == '__main__':
    unittest.main()
