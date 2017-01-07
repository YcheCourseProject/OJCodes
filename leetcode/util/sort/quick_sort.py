import random
import unittest


# in place sorting
def quick_sort(num_list):
    if len(num_list) > 1:
        quick_sort_detail(num_list, 0, len(num_list))


def quick_sort_detail(num_list, begin, end):
    if end - begin <= 0:
        return
    else:
        pivot_idx = end - 1
        left_idx, right_idx = begin, pivot_idx - 1
        while True:
            while num_list[left_idx] < num_list[pivot_idx] and left_idx <= right_idx:
                left_idx += 1
            while num_list[right_idx] > num_list[pivot_idx] and right_idx >= left_idx:
                right_idx -= 1

            if left_idx < right_idx:
                num_list[left_idx], num_list[right_idx] = num_list[right_idx], num_list[left_idx]
            else:
                num_list[pivot_idx], num_list[left_idx] = num_list[left_idx], num_list[pivot_idx]
                quick_sort_detail(num_list, begin, left_idx)
                quick_sort_detail(num_list, left_idx + 1, end)
                return


class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        for i in range(100):
            my_list = range(i)
            expected_list = range(i)
            random.shuffle(my_list)
            quick_sort(my_list)
            self.assertListEqual(my_list, expected_list)


if __name__ == '__main__':
    unittest.main()
