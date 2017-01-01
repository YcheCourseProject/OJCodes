class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution1(object):
    def twoSum(self, nums, target):
        ele_dict = dict()
        for idx, ele in enumerate(nums):
            ele_dict[ele] = idx

        for i in xrange(len(nums)):
            if target - nums[i] in ele_dict:
                j = ele_dict[target - nums[i]]
                if j != i:
                    return [i, j]


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    print Solution1().twoSum(nums, target)
