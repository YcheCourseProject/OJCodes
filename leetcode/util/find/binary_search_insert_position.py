import random
import unittest


def binary_search_detail(num_list, begin, end, target_val, alternative_idx):
    if begin == end:
        return max(begin, alternative_idx)
    else:
        med_idx = (begin + end) / 2
        if target_val == num_list[med_idx]:
            return med_idx
        elif target_val < num_list[med_idx]:
            return binary_search_detail(num_list, begin, med_idx, target_val, med_idx)
        else:
            return binary_search_detail(num_list, med_idx + 1, end, target_val, med_idx)


def binary_search(num_list, target_val):
    return binary_search_detail(num_list, 0, len(num_list), target_val, len(num_list))


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_recursion(self):
        for round_num in xrange(1000):
            num_list = sorted(random.sample(range(100), 10))
            for i in range(10):
                search_val = random.randint(-1, 100)
                idx = binary_search(num_list, search_val)
                if idx == len(num_list):
                    self.assertTrue(search_val >= num_list[len(num_list) - 1])
                elif idx == 0:
                    self.assertTrue(search_val <= num_list[0])
                else:
                    self.assertTrue(num_list[idx - 1] <= search_val <= num_list[idx])


if __name__ == '__main__':
    unittest.main()
