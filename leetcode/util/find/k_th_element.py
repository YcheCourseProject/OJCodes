import random
import unittest


def k_th_element(num_list, k):
    if k < 0 or k >= len(num_list):
        return None
    else:
        return k_th_element_detail(num_list, 0, len(num_list), k)


def k_th_element_detail(num_list, begin, end, k):
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
            if left_idx == begin + k:
                return num_list[left_idx]
            elif left_idx > begin + k:
                return k_th_element_detail(num_list, begin, left_idx, k)
            else:
                return k_th_element_detail(num_list, left_idx + 1, end, k - (left_idx + 1 - begin))


class TestKthElement(unittest.TestCase):
    def test_kth_element(self):
        for i in range(100):
            my_list = range(i)
            random.shuffle(my_list)

            expected_list = range(i)
            ret_list = [k_th_element(my_list, j) for j in range(i)]
            self.assertListEqual(ret_list, expected_list)


if __name__ == '__main__':
    unittest.main()
