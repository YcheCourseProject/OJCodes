class NaiveSolution(object):
    @staticmethod
    def merge_two(left, right):
        nums3 = []
        idx_left = 0
        idx_right = 0
        while idx_left < len(left) or idx_right < len(right):
            print idx_left, idx_right
            if idx_right == len(right):
                nums3.append(left[idx_left])
                idx_left += 1
            elif idx_left == len(left):
                nums3.append(right[idx_right])
                idx_right += 1
            elif left[idx_left] < right[idx_right]:
                nums3.append(left[idx_left])
                idx_left += 1
            else:
                nums3.append(right[idx_right])
                idx_right += 1
        nums3 = map(float, nums3)
        return nums3

    def findMedianSortedArrays(self, left, right):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = NaiveSolution.merge_two(left, right)
        return (nums3[(len(nums3) - 1) / 2] + nums3[len(nums3) / 2]) / 2


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print NaiveSolution().findMedianSortedArrays(nums1, nums2)
