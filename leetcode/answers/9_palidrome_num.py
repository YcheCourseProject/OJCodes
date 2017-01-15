import math


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            digit_max_idx = int(math.floor(math.log10(x)))
            first_digit = x / (10 ** digit_max_idx)
            last_digit = x % 10
            if first_digit != last_digit:
                return False
            else:
                remain = (x - last_digit - first_digit * (10 ** digit_max_idx)) / 10
                if remain < 10 ** (digit_max_idx - 2):
                    remain += 10 ** (digit_max_idx - 2) + 1
                return self.isPalindrome(remain)


if __name__ == '__main__':
    print Solution().isPalindrome(1000021)
    print Solution().isPalindrome(1000110001)
