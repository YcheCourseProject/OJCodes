import time


class Solution(object):
    @staticmethod
    def binary_search(arr, beg, end, val):
        if beg >= end:
            return -1

        while end - beg >= 1:
            mid = beg + (end - beg) / 2
            if arr[mid] == val:
                return mid
            elif arr[mid] < val:
                beg = mid + 1
            else:
                end = mid
        return -1

    def threeSumTLE(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        more_than_once_set = set()
        prev = None
        for num in sorted_nums:
            if prev == num:
                more_than_once_set.add(num)

        candidate_lst = []
        computation_set = set()
        for i in xrange(len(sorted_nums) - 2):
            for j in xrange(i + 1, len(sorted_nums) - 1):
                if (sorted_nums[i], sorted_nums[j]) not in computation_set:
                    computation_set.add((sorted_nums[i], sorted_nums[j]))
                    idx = Solution.binary_search(sorted_nums, j + 1, len(sorted_nums), -sorted_nums[i] - sorted_nums[j])
                    if idx != -1:
                        candidate_lst.append([sorted_nums[i], sorted_nums[j], sorted_nums[idx]])

        return candidate_lst

    def threeSumTLEHashSet(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)

        # for non-zeros
        more_than_once_set = set()
        prev = None
        for num in sorted_nums:
            if prev == num:
                more_than_once_set.add(num)
            prev = num

        candidate_lst = []
        if len(filter(lambda val: val == 0, sorted_nums)) >= 3:
            candidate_lst.append([0, 0, 0])

        computation_set = set()
        computation_set.add((0, 0))
        sorted_nums_set = set(nums)
        for i in xrange(len(sorted_nums) - 2):
            for j in xrange(i + 1, len(sorted_nums) - 1):
                if (sorted_nums[i], sorted_nums[j]) not in computation_set:
                    computation_set.add((sorted_nums[i], sorted_nums[j]))
                    third_num = -sorted_nums[i] - sorted_nums[j]
                    if third_num in sorted_nums_set:
                        if third_num > sorted_nums[j] or (
                                third_num == sorted_nums[j] and third_num in more_than_once_set):
                            candidate_lst.append([sorted_nums[i], sorted_nums[j], third_num])

        return candidate_lst


if __name__ == '__main__':
    # S = [-1, 0, 1, 2, -1, -4]
    # S = [0, 0, 0]
    # S = [0, 0]
    # S = [-1, 0, 1, 0]
    with open('data/15_3sum.txt') as ifs:
        S = eval(''.join(ifs.readlines()))

    start = time.time()
    print Solution().threeSumTLE(S)
    end = time.time()
    print end - start

    start = time.time()
    print Solution().threeSumTLEHashSet(S)
    end = time.time()
    print end - start
